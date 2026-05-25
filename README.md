# DevelopersHub Corporation — AI/ML Engineering Internship

This repository documents my progressive work, datasets, and models implemented during the AI/ML Engineering Internship at DevelopersHub Corporation. 

**Intern Name:** Areej Fatima  
**Academic Program:** BS Information Technology (Morning A, 2023–2027)  
**Submission Date:** June 2026  

---

## Task 1: Exploring and Visualizing the Iris Dataset

### Objective
To establish strong foundations in Exploratory Data Analysis (EDA) by programmatically loading, inspecting, summarizing, and visually modeling feature correlations and distributions within the classic Iris flower dataset.

### Tech Stack & Environment
- **IDE:** Visual Studio Code (VS Code) utilizing a local Jupyter Notebook kernel
- **Environment Management:** Isolated virtual environment (`.venv`) for package reproducibility
- **Libraries Used:** - `pandas` (Structured data analysis and structural aggregation)
  - `matplotlib` (Base visualization engine)
  - `seaborn` (Statistical visualization and theme layer)

### Key Insights & Analytical Findings

1. **Feature Relationships (Scatter Plot Analysis):**
   - Plotting **Petal Length vs. Petal Width** reveals distinct clustering patterns across the species.
   - *Iris setosa* forms a entirely isolated structural cluster with smaller petal profiles.
   - *Iris versicolor* and *Iris virginica* exhibit a close spatial trend line, proving a strong continuous linear correlation between petal width and length across morphing species.

2. **Data Distribution (Histogram & KDE Analysis):**
   - Utilizing continuous **Kernel Density Estimate (KDE)** lines over feature density histograms verified that **Sepal Length** approximates normal distributions for individual classes.
   - *Iris virginica* consistently showcases the highest concentration of extended sepal lengths, while *Iris setosa* maps to tightly grouped lower distributions.

3. **Outlier Identification (Box Plot Analysis):**
   - The categorical box plot isolated distinct statistical anomalies across **Sepal Width** values.
   - Individual observations extending beyond the standard whiskers ($1.5 \times \text{IQR}$) inside the *Iris setosa* category flag clear target outliers requiring consideration during subsequent machine learning training pipelines.

---

### How to Run the Notebook Local Environment

1. Clone this repository to your workstation:
   ```bash
   git clone https://github.com/dreams-from-dust/DevelopersHub-AI-ML-Internship
   cd DevelopersHub-Internship

2. Activate the localized virtual environment:
   ```powershell
   .venv\Scripts\Activate.ps1

3. Open VS Code and execute the notebook `Iris_EDA.ipynb` cell-by-cell.

## Task 4: General Health Query Informatics Platform

### Objective
To engineer a secure, low-latency health literacy interface utilizing advanced system prompt engineering to deliver medical educational insights while systematically enforcing clinical safety guardrails.

### Tech Stack & Environment
- **Interface Framework:** Streamlit (Theme-adaptive enterprise layout)
- **Inference Engine:** Groq LPU Hardware Cluster
- **Large Language Model:** Llama-3.1-8b-Instant
- **Temperature Configuration:** 0.3 (Optimized to mitigate token hallucination)

### Safety Guardrails Enforced
1. **Diagnostic Prohibition:** Systematically suppresses attempts to confirm specific patient pathologies.
2. **Pharmaceutical Restriction:** Explicitly restricts the calculation or dissemination of drug dosages.
3. **Emergency Escalation:** Detects acute, life-threatening symptoms and triggers immediate directives to contact local emergency services.

### How to Launch the Interface

1. Ensure your localized virtual environment is active:
   ```powershell
   .venv\Scripts\Activate.ps1

2. Install the production dependencies:
   ```bash
   pip install groq streamlit

3. Execute the Streamlit server command:
   ```bash
   streamlit run Health_Chatbot.py
