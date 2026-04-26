import pandas as pd

def create_skills_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a normalized skills dataframe from cleaned jobs dataframe.

    Parameters:
        df (pd.DataFrame): Cleaned jobs dataframe

    Returns:
        pd.DataFrame: skills_df with columns:
                      job_id, job_title_short, category, skill
    """

    # Select only required columns to reduce memory usage and improve clarity
    df_temp = df[['job_id', 'job_title_short', 'job_type_skills']].copy()

    # Convert dictionary column into list of (category, skills_list) tuples
    # Example: {"programming": ["python", "sql"]} → [("programming", ["python", "sql"])]
    # If value is not a dict (e.g., NaN), replace with empty list to avoid errors
    df_temp['items'] = df_temp['job_type_skills'].apply(
        lambda d: list(d.items()) if isinstance(d, dict) else []
    )

    # Explode list so each row contains one (category, skills_list) pair
    df_temp = df_temp.explode('items')

    # Remove rows where items is null (i.e., no skills data available)
    df_temp = df_temp.dropna(subset=['items'])

    # Create explicit copy to avoid SettingWithCopyWarning before assignment
    df_temp = df_temp.copy()

    # Split tuple into two separate columns: category and skills (list)
    df_temp[['category', 'skills']] = pd.DataFrame(
        df_temp['items'].tolist(),
        index=df_temp.index
    )

    # Explode skills list so each row contains a single skill
    # Also drop null values that may exist inside lists
    df_temp = df_temp.explode('skills').dropna(subset=['skills'])

    # Clean skill names by removing leading/trailing whitespace and Standardize skill names
    df_temp['skills'] = df_temp['skills'].str.strip().str.lower()

    # Select final columns and rename for clarity
    skills_df = df_temp[
        ['job_id', 'job_title_short', 'category', 'skills']
    ].rename(columns={'skills': 'skill'})

    # Remove duplicate (job_id, skill) combinations
    # Ensures same skill is not counted multiple times for a job
    skills_df = skills_df.drop_duplicates(subset=['job_id', 'skill'])

    return skills_df