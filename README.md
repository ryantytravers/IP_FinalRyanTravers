# Contract Clause Classification Project

This project classifies commercial contract clauses into four standard legal categories: Confidentiality, Termination, Governing Law, and Non-Compete.

## Project Structure
* contract_clauses_1200.csv: The balanced dataset containing 1,200 labeled contract clauses.
* evaluate.py: The script that runs the baseline and trains Logistic Regression, Naive Bayes, and Linear SVM models.
* app.py: A Streamlit web application providing an interactive interface to test clauses.
* requirements.txt: Python package requirements.

## How to Set Up and Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run model evaluations:
   python evaluate.py

3. Run the interactive demo:
   streamlit run app.py

## Model Evaluation Results
* Rule-Based Baseline: 71.67% Accuracy | 0.6656 Macro F1
* Logistic Regression: 100.00% Accuracy | 1.0000 Macro F1
* Multinomial Naive Bayes: 100.00% Accuracy | 1.0000 Macro F1
* Linear SVM: 100.00% Accuracy | 1.0000 Macro F1

## Disclosure of AI Assistance
AI assistance was used to help troubleshoot scikit-learn pipeline syntax, organize repository documentation, and structure evaluation metrics. All dataset curation, model execution, and reported findings reflect actual work run locally.