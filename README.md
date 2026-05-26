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
- **Development & Logging Kernel:** Jupyter Notebook (`Task_4_Inference.ipynb`)

### Deliverables & Repository Structure
- **`Health_Chatbot.py`**: The live frontend Streamlit application source code.
- **`Task_4_Inference.ipynb`**: Companion development notebook logging prompt validation, guardrail behaviors, and raw API response structures.

### Safety Guardrails Enforced
1. **Diagnostic Prohibition:** Systematically suppresses attempts to confirm specific patient pathologies.
2. **Pharmaceutical Restriction:** Explicitly restricts the calculation or dissemination of drug dosages.
3. **Emergency Escalation:** Detects acute, life-threatening symptoms and triggers immediate directives to contact local emergency services.

### How to Run and Launch

#### 1. Running the Academic Notebook
To view the underlying prompt architecture and integration test results directly within a notebook kernel:
- Open your workspace in VS Code.
- Select your virtual environment kernel (`.venv`) and open `Health_Chatbot_Inference.ipynb`.
- Execute the cells sequentially to observe backend model inference.

#### 2. Launching the Interactive Web Interface
To spin up the web dashboard, ensure your localized virtual environment is active and follow these steps:

1. Activate your environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. Install the production dependencies:
   ```bash
   pip install groq streamlit
   ```

* **Health Chatbot:**
  ```bash
  streamlit run Task_4_Health_Chatbot/Health_Chatbot.py
  ```

---

### Methodology


This project follows the industry-standard AI/ML engineering pipeline:

1. **Data Acquisition:** Sourcing clean, relevant datasets from trusted repositories (e.g., Kaggle, CSV files).
2. **Preprocessing:** Performing data cleaning, feature engineering, and robust feature scaling to prepare data for model consumption.
3. **Modeling:** Selection and iterative training of appropriate regression or classification architectures to solve specific problem sets.
4. **Deployment:** Wrapping finalized models into interactive, production-ready web-based interfaces (Streamlit) for end-user validation and testing.
