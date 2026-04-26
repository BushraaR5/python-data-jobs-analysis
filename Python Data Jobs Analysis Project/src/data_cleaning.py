"""
Data Cleaning Pipeline for Job Listings Dataset

Steps:
1. Load raw data
2. Clean and standardize fields
3. Parse nested columns
4. Generate unique job IDs
5. Merge duplicate job postings
6. Output clean dataset for analysis
"""

# Import required libraries
from pathlib import Path
import pandas as pd
import ast
import hashlib
from collections import defaultdict


def load_and_clean_data(filepath=None,save=False):
    """
    Loads raw job data, cleans it, removes duplicates, and generates a unique job_id.
    Returns a standardized DataFrame for further analysis.
    """
    # Define project root (Python Project/)
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Default paths
    raw_path = BASE_DIR / "data" / "raw" / "data_jobs.csv"
    sample_path = BASE_DIR / "data" / "raw" / "data_jobs_sample.csv"

    # Decide which file to use
    if filepath is None:
        if raw_path.exists():
            filepath = raw_path
            print("Using full dataset")
        elif sample_path.exists():
            filepath = sample_path
            print("Using sample dataset")
        else:
            raise FileNotFoundError("No dataset found in data/raw or data/")
    else:
        filepath = Path(filepath)

    # =========================
    # 1. Load Data
    # =========================
    df = pd.read_csv(filepath)

    # =========================
    # 2. Basic Cleaning
    # =========================

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Convert job_posted_date to datetime format
    df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

    # Clean 'job_via' column by removing 'via ' prefix
    df['job_via'] = df['job_via'].str.replace('via ', '')

    # =========================
    # 3. Parse String Columns
    # =========================

    # Convert job_skills from string → list
    def safe_parse(x):
        try:
            return ast.literal_eval(x) if isinstance(x, str) else []
        except:
            # Mark rows where parsing fails
            return ['PARSE_ERROR']

    df['job_skills'] = df['job_skills'].apply(safe_parse)

    # Convert job_type_skills from string → dictionary
    def parse_dict(x):
        try:
            return ast.literal_eval(x) if isinstance(x, str) else {}
        except:
            return {'PARSE_ERROR'}

    df['job_type_skills'] = df['job_type_skills'].apply(parse_dict)

    # =========================
    # 4. Generate Unique Job ID
    # =========================

    def generate_job_id(row):
        """
        Create a unique ID using key job attributes.
        Helps in deduplication and merging similar postings.
        """

        title_short = str(row['job_title_short']).strip().lower() if pd.notna(row['job_title_short']) else ''
        title = str(row['job_title']).strip().lower() if pd.notna(row['job_title']) else ''
        company = str(row['company_name']).strip().lower() if pd.notna(row['company_name']) else ''
        job_location = str(row['job_location']).strip().lower() if pd.notna(row['job_location']) else ''
        search_location = str(row['search_location']).strip().lower() if pd.notna(row['search_location']) else ''
        job_date = str(row['job_posted_date']).strip().lower() if pd.notna(row['job_posted_date']) else ''

        # Combine fields into a single string
        text = f"{title_short}|{title}|{company}|{job_location}|{search_location}|{job_date}"

        # Generate hash-based ID
        return 'J-' + hashlib.md5(text.encode('utf-8')).hexdigest()[:12]

    df['job_id'] = df.apply(generate_job_id, axis=1)

    # =========================
    # 5. Merge Duplicate Job Entries
    # =========================

    # Merge job_skills → flatten and remove duplicates
    merged_skills = df.groupby('job_id')['job_skills'].apply(
        lambda x: sorted(set(skill for sublist in x for skill in sublist))
    )

    # Merge job_via → keep unique platforms
    merged_via = df.groupby('job_id')['job_via'].apply(
        lambda x: list(set(x))
    )

    # Merge salary_rate → take first non-null value
    merged_rate = df.groupby('job_id')['salary_rate'].apply(
        lambda x: next((v for v in x if pd.notna(v)), None)
    )

    # Merge job_type_skills → combine dictionaries and deduplicate values
    merged_job_type_skills = {}

    for job_id, group in df.groupby('job_id'):
        merged = defaultdict(set)

        for d in group['job_type_skills']:
            if isinstance(d, dict):
                for key, values in d.items():
                    if isinstance(values, list):
                        merged[key].update(values)

        # Convert sets → sorted lists
        merged_job_type_skills[job_id] = {k: sorted(v) for k, v in merged.items()}

    # =========================
    # 6. Map Merged Values Back
    # =========================

    df['job_skills'] = df['job_id'].map(merged_skills)
    df['job_via'] = df['job_id'].map(merged_via)
    df['salary_rate'] = df['job_id'].map(merged_rate)
    df['job_type_skills'] = df['job_id'].map(merged_job_type_skills)

    # =========================
    # 7. Final Deduplication
    # =========================

    # Keep only one row per unique job_id
    df = df.drop_duplicates(subset='job_id')
    
    # Optional save as csv
    if save:
        output_dir = BASE_DIR / "data" / "processed"

        # Ensure folder exists (important!)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save files
        df.to_csv(output_dir / "cleaned_jobs.csv", index=False)
        df.to_pickle(output_dir / "cleaned_jobs.pkl")
        df.to_parquet(output_dir / "cleaned_jobs.parquet")
    
    return df

def load_csv_with_parsing(filepath=None):
    """
    Load cleaned CSV and restore list/dict columns
    """

    # Define project root
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Default path
    if filepath is None:
        filepath = BASE_DIR / "data" / "processed" / "cleaned_jobs.csv"
    else:
        filepath = Path(filepath)

    df = pd.read_csv(filepath)

    df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    df['job_type_skills'] = df['job_type_skills'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    return df