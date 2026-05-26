# DevelopersHub Corporation — AI/ML Engineering Internship
**Intern Name:** Areej Fatima | **Submission Date:** 05June 2026

This repository serves as the official submission for the AI/ML Engineering Internship at DevelopersHub Corporation. It documents my implementation of data analysis, regression modeling, and Generative AI applications.

---

## Project Structure & Task Mapping

This repository includes the internship deliverables for Task 1, Task 4, and Task 6.

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

### How to Run the Internship Tasks

1. Clone this repository to your workstation:
   ```bash
   git clone https://github.com/dreams-from-dust/DevelopersHub-AI-ML-Internship
   cd DevelopersHub-Internship
   ```

2. Activate the localized virtual environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the shared dependencies used across the tasks:
   ```bash
   pip install pandas seaborn numpy scikit-learn plotly streamlit
   ```

---

## Task 1: Exploratory Data Analysis (Iris Dataset)

- Open `Task1_Iris_EDA/Iris_EDA.ipynb` in VS Code or Jupyter.
- Select the `.venv` Python kernel.
- Execute the notebook cells sequentially to walk through data loading, cleaning, visualization, and statistical summarization.
- The notebook includes plots and analysis for sepal/petal distributions, species separation, and correlation insights.

---

## Task 4: General Health Chatbot

- Open `Task4_Health_Chatbot/Health_Chatbot.py`.
- Install the required inference dependency if not already installed:
  ```bash
  pip install groq streamlit
  ```
- Launch the interactive dashboard:
  ```bash
  streamlit run Task4_Health_Chatbot/Health_Chatbot.py
  ```
- This app demonstrates prompt-engineered safety guardrails, medical education responses, and a secure inference workflow.

---

## Task 6: House Price Prediction

- Open `Task6_House_Price_Prediction/House_Price_Prediction.ipynb` in VS Code or Jupyter to inspect the model training and evaluation pipeline.
- Alternatively, run the Streamlit interface if you want an interactive valuation demo:
  ```bash
  streamlit run Task6_House_Price_Prediction/house_price_app.py
  ```
- The task uses a regression model with feature preprocessing, pricing benchmarks, and dual-currency USD/PKR valuation outputs.

---

### Methodology

#### Task 1 Methodology: Exploratory Data Analysis
- Collected and loaded the Iris dataset into a pandas DataFrame.
- Performed data inspection, summary statistics, and missing-value validation.
- Visualized feature distributions and species relationships using seaborn and matplotlib.
- Identified patterns, correlations, and class separation to support analysis conclusions.

#### Task 4 Methodology: Health Chatbot Engineering
- Designed system prompt guardrails to enforce safe, non-diagnostic medical responses.
- Developed a Streamlit interface for interactive user queries and secure backend inference.
- Integrated a language model via the Groq API for low-latency educational health guidance.
- Implemented conversational state storage and user-facing disclaimers to maintain transparency.

#### Task 6 Methodology: House Price Prediction
- Generated or loaded housing feature data and engineered derived variables such as bed/bath ratio.
- Applied preprocessing using standard scaling and one-hot encoding for categorical location data.
- Trained a HistGradientBoostingRegressor pipeline to model pricing behavior.
- Created an interactive Streamlit app to present valuation estimates and dual-currency analytics.

## Task Coverage & Submission Summary

- **Completed Tasks:** Task 1, Task 4, and Task 6 are fully documented and available in this repository.
- **Notebook and Code Artifacts:** Each task includes a dedicated notebook or app with step-by-step explanations, dataset preparation, modeling or prompt engineering, and results discussion.
- **Task 1 Notebook:** `Task1_Iris_EDA/Iris_EDA.ipynb` contains the problem statement, dataset loading, exploratory analysis, visualization, and summary insights.
- **Task 4 App & Notebook:** `Task4_Health_Chatbot/Health_Chatbot.py` and the companion notebook document the health chatbot design, safety guardrails, and interface workflow.
- **Task 6 Notebook & Demo:** `Task6_House_Price_Prediction/House_Price_Prediction.ipynb` includes feature engineering, model training, evaluation metrics, and conclusions; `house_price_app.py` demonstrates an interactive valuation interface.
- **Code Quality and Documentation:** Code is organized for readability, with comments or markdown explanations for each key step and clear task objectives.
- **Repository Submission:** This README provides a task summary, run instructions, and methodology for the internship deliverables.

---
