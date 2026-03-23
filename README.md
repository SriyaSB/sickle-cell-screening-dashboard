# Sickle Cell Disease Screening Dashboard
This project simulates a screening programme for sickle cell disease (SCD) in Odisha and Assam, India. Using synthetic data based on recent research, I built an interactive dashboard to monitor key indicators: screening coverage, awareness, treatment uptake, and lost‑to‑follow‑up.

# Motivation
The job focuses on screening, diagnosis, treatment, and care for SCD – a major public health issue in tribal populations. This dashboard shows I can:
- Understand the real‑world context of SCD in Odisha/Assam.
- Work with data (demographics, clinical, screening, treatment).
- Build a practical tool to monitor a screening programme.
- Apply public health and implementation research principles.

# Data Source
The synthetic dataset was generated using parameters from four recent papers (2024‑2026):
- *Dutta et al. (2024)* – Clinical profile and treatment patterns in Upper Assam.
- *Mishra et al. (2025)* – Awareness and screening in Sundargarh, Odisha.
- *Bindhani et al. (2024)* – Knowledge, attitudes, and practices in Koraput, Odisha.
- *Rajamani et al. (2025)* – Barriers to newborn screening (ICMR multicentric study).
- *Arora (2026)* – Digital architecture of India’s National SCD Mission.
All synthetic variables (age, genotype, symptoms, awareness, treatment, etc.) reflect the real proportions from these studies.

# Methodology
1. *Data generation* – Python script (`generate_synthetic_data.py`) creates 800 patient records in "scd_screening_data.csv".
2. *Analysis* – Descriptive statistics, chi‑square tests, t‑tests (in `analysis.py`) (analysis_output.txt).
3. *Dashboard* – Streamlit app (`dashboard.py`) provides interactive visualisations.

# Key Findings
- Only **45%** of individuals had heard of SCD.
- Screening coverage overall is **47%**, varying by district.
- Among HbSS patients, only **50%** are on hydroxyurea.
- **16%** are lost to follow‑up (inactive for 3 months).
- No significant association was found between belief in black magic and screening uptake (p = 0.94), though qualitative studies suggest this is a real barrier.

# Dashboard Screenshots

*Screening coverage by district*
![Screening coverage]![Image](https://github.com/user-attachments/assets/321174fa-f23d-42d1-9aec-06f69a0f0c82)

*Awareness levels*
![Awareness]![Image](https://github.com/user-attachments/assets/2f374991-a3b0-481e-87f5-da9c027a646d)

*Cascade of care*
![Cascade](![Image](https://github.com/user-attachments/assets/aac3bf02-ba89-4cf6-bc15-5451164740a9))

*Lost to follow‑up list*
![LTFU](screenshots/ltfu.jpg)
# Repository Structure

- *[generate_synthetic_data.py](generate_synthetic_data.py)** – Creates the synthetic dataset.
- *[dashboard.py](dashboard.py)** – Streamlit dashboard.
- *[analysis.py](analysis.py)** – Statistical analysis.
- *[analysis_output.txt](analysis_output.txt)** – Python dependencies.
- *[scd_screening_data.csv](scd_screening_data.csv)** – Generated dataset.
