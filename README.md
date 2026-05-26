# DevelopersHub Corporation — AI/ML Engineering Internship
**Intern Name:** Areej Fatima | **Submission Date:** 05June 2026

This repository serves as the official submission for the AI/ML Engineering Internship at DevelopersHub Corporation. It documents my implementation of data analysis, regression modeling, and Generative AI applications.

---

## Project Structure & Task Mapping

| Task | Objective | Dataset | Model/Tool Applied |
| :--- | :--- | :--- | :--- |
| **Task 1** | Exploratory Data Analysis | Iris Dataset | `Pandas`, `Seaborn` |
| **Task 4** | General Health Chatbot | Prompt Engineering | `Llama-3.1-8b` (Groq API) |
| **Task 6** | House Price Prediction | Property Features | `HistGradientBoostingRegressor` |

---

## Detailed Task Summaries

### Task 1: Exploratory Data Analysis (Iris Dataset)
* **Objective:** Establish foundations in EDA by loading, inspecting, and visualizing structural data distributions.
* **Dataset:** Iris Flower Dataset (150 samples).
* **Models/Tools:** `pandas` for statistics, `seaborn`/`matplotlib` for visual correlation analysis.
* **Key Results:** Successfully identified distinct species clusters and verified normal distributions of sepal/petal dimensions.

### Task 4: Health Query Chatbot
* **Objective:** Develop a secure, empathetic chatbot providing educational medical information while enforcing safety protocols.
* **Dataset:** Prompt-engineered context for medical education.
* **Models/Tools:** `Llama-3.1-8b-instant` via Groq API.
* **Key Results:** Implemented "Diagnostic Prohibition" and "Pharmaceutical Restriction" system prompts to ensure safe, non-harmful educational interactions.

### Task 6: House Price Prediction
* **Objective:** Predict real estate values based on property features using regression modeling.
* **Dataset:** House Price Prediction Dataset (1,500 samples).
* **Models/Tools:** `HistGradientBoostingRegressor` (Scikit-Learn).
* **Key Results:** Achieved high predictive accuracy with localized pricing metrics. Deployed a production-ready interface using Streamlit.

---

## Execution Guide

### 1. Environment Setup
To reproduce this project locally, ensure you have Python installed and run the following in your terminal:
```bash
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt 
```

### 2. Launching Interactive Interfaces
To launch the application dashboards in your local browser, execute the following commands in your terminal:

* **House Price Engine:**
  ```bash
  streamlit run Task_6_House_Price_Prediction/house_price_app.py

* **Health Chatbot:**
  ```bash
streamlit run Task_4_Health_Chatbot/Health_Chatbot.py

---

### Methodology


This project follows the industry-standard AI/ML engineering pipeline:

1. **Data Acquisition:** Sourcing clean, relevant datasets from trusted repositories (e.g., Kaggle, CSV files).
2. **Preprocessing:** Performing data cleaning, feature engineering, and robust feature scaling to prepare data for model consumption.
3. **Modeling:** Selection and iterative training of appropriate regression or classification architectures to solve specific problem sets.
4. **Deployment:** Wrapping finalized models into interactive, production-ready web-based interfaces (Streamlit) for end-user validation and testing.
