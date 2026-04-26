# 📊 Python Data Jobs Analysis

🚀 End-to-end data analysis project exploring job market trends, skills demand, and salary insights in the data industry.

## 📌 Project Overview

This project performs an end-to-end analysis of real-world data job postings to uncover:

- 🛠️ In-demand skills across roles  
- 👤 Role-based skill requirements  
- 💰 Salary trends and growth  
- 🌍 Job market structure (remote work, platforms, hiring patterns) 

The goal is to help aspiring data professionals understand the current job market and make informed career decisions.

---

## 📊 Dataset

This project uses the **Data Jobs Dataset** created by Luke Barousse.

- Source: https://huggingface.co/datasets/lukebarousse/data_jobs

This dataset contains real-world data analytics job postings collected from multiple sources using automated scraping methods. :contentReference[oaicite:0]{index=0}

### ⚠️ Data Availability Note

The full dataset (~230MB+) is not included in this repository due to size limitations.

Instead:
- A **sample dataset** is provided for demonstration
- All notebooks and scripts are designed to:
  - Use the full dataset if available
  - Automatically fall back to the sample dataset

This ensures the project runs smoothly for anyone cloning the repository.

---

## 📥 Load Full Dataset

To reproduce full results, load the dataset using:

```python
import pandas as pd
from datasets import load_dataset

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

```

## 📁 Folder Structure

```
python-data-jobs-analysis/
│
├── data/
│   ├── raw/
│   │   └── data_jobs_sample.csv
│   └── processed/
│
├── notebooks/
│   ├── 1.data_cleaning.ipynb
│   ├── 2.skills_analysis.ipynb
│   ├── 3.role_analysis.ipynb
│   ├── 4.salary_analysis.ipynb
│   └── 5.job_market_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   └── skills_processing.py
│
└── README.md
```

## 🔍 Analysis Breakdown

The analysis is divided into four key components:

### 1️⃣ Skills Analysis
- Identifies the most in-demand skills globally
- Groups skills into categories (programming, cloud, tools)
- Highlights learning priorities

### 2️⃣ Role Analysis
- Compares Data Analyst, Data Engineer, and Data Scientist roles
- Examines skill distribution and role expectations
- Analyzes salary benchmarks and growth

### 3️⃣ Salary Analysis
- Links skills with salary outcomes
- Identifies high-paying vs low-paying skills
- Compares salary distributions and geography

### 4️⃣ Job Market Analysis
- Explores hiring patterns (full-time vs contract)
- Analyzes job platforms and remote trends
- Tracks demand over time

📌 **Key Insights** 

### 🛠️ Skills
- Python and SQL dominate the market (~19% each)
- Cloud skills (AWS, Azure) significantly increase salary potential
- Specialized tools (Spark, Kafka) are niche but high-paying

<img width="1487" height="803" alt="image" src="https://github.com/user-attachments/assets/e03da98b-c56c-493c-a216-25bd1c289276" />

### 👤 Roles
- Data Scientists earn the highest salaries (~$155K senior level)
- Data Engineers offer strong demand + salary balance
- Data Analysts have highest job volume but lower pay

<img width="1482" height="648" alt="image" src="https://github.com/user-attachments/assets/a9e244b5-20c9-451f-a699-116eb77c81ae" />

### 💰 Salary
- High-paying roles are strongly linked to:
  - Cloud technologies
  - Big data tools
- Remote roles offer higher average salaries (~10–15% more)

<img width="1488" height="755" alt="image" src="https://github.com/user-attachments/assets/db5fac61-4c1c-43b7-919c-6ab45129ff7a" />

### 🌐 Job Market
- ~90% of roles are full-time
- LinkedIn dominates job postings
- Remote work is increasing, especially in higher-paying roles

<img width="1127" height="780" alt="image" src="https://github.com/user-attachments/assets/f54b444a-1e78-46fb-b19b-993e50806ce3" />

## 🎯 Why This Project Matters

This project provides a **data-driven roadmap** for:

### 👨‍💻 Aspiring Data Professionals
- What to learn first
- Which roles to target
- How to increase earning potential

### 💼 Job Seekers
- Which platforms to focus on
- How remote work impacts salary
- Where opportunities are growing

### 🏢 Recruiters / Businesses
- Understanding talent demand
- Identifying high-value skill gaps

---

## 💡 What This Project Demonstrates

- End-to-end data analysis workflow
- Data cleaning and preprocessing of real-world datasets
- Exploratory data analysis (EDA)
- Feature engineering (skills extraction, salary mapping)
- Business insight generation from data

---

## 🛠 Tools & Technologies

- Python (Pandas, NumPy)
- Data Visualization (Matplotlib, Seaborn)
- Jupyter Notebook
- Data Cleaning & Transformation

---

## ▶️ How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install pandas matplotlib seaborn datasets
   ```
3. Run the notebooks in order

---

## 📌 Conclusion

The data job market rewards:
- Strong foundations (Python + SQL)
- Strategic specialization (Cloud, Big Data)
- Smart role selection

---

## 🙌 Acknowledgment

Dataset provided by **Luke Barousse**
https://huggingface.co/datasets/lukebarousse/data_jobs

---

## 📬 Contact

- GitHub: https://github.com/BushraaR5  
- LinkedIn: (to be updated) 
- Upwork: (to be updated)

Feel free to reach out for data analysis or Power BI projects.

If you found this project useful or have feedback, feel free to connect!
