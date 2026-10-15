# Contract Clause Classifier

This project uses machine learning to sort contract paragraphs into four categories:
- **Confidentiality**
- **Termination**
- **Governing Law**
- **Non-Compete**

Reading long business contracts by hand takes a long time. Simple keyword searches often miss things if a sentence does not use the exact word you searched for. This project tests if machine learning models can do a better job, and includes a simple web app to test out sentences.

---

## Results

I tested a simple keyword search against three machine learning models using unseen test contracts:

- **Keyword Search:** 88% accuracy (0.9286 Macro F1)
- **Naive Bayes:** 94% accuracy (0.9365 Macro F1)
- **Support Vector Machine:** 94% accuracy (0.9365 Macro F1)
- **Logistic Regression:** 94% accuracy (0.9365 Macro F1)

### What I Learned
- **Keyword search fails on indirect phrasing:** If a contract says "the agreement will end" instead of using the word "terminate," a keyword search misses it. The machine learning models correctly caught these.
- **Where the model struggled:** A technical engineering rule got mistaken for Confidentiality because it had words like "server cores" and "processor design" instead of normal legal words like "compete."

---

## Files in This Project

- `contract_clauses_1200.csv`: The dataset of 1,200 contract paragraphs (300 for each category) taken from public SEC filings.
- `evaluate.py`: The Python script that trains the models and prints the scores.
- `app.py`: The web app code where you can type or paste a sentence and see the prediction.
- `build_dataset.py`: The script used to pull and clean the data.
- `requirements.txt`: The list of Python libraries needed to run the project.

---

## How to Run It

### 1. Install packages
```bash
pip install -r requirements.txt