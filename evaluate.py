import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

df = pd.read_csv("contract_clauses_1200.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["category"], test_size=240, random_state=42, stratify=df["category"]
)

KEYWORD_RULES = {
    "Confidentiality": ["confidential", "proprietary", "non-disclosure", "trade secret", "disclose"],
    "Termination": ["terminate", "termination", "cancel", "cure period", "default", "breach"],
    "Governing Law": ["governing law", "jurisdiction", "laws of the state", "construed in accordance with"],
    "Non-Compete": ["non-compete", "covenant not to compete", "solicit", "restricting", "competitive business"]
}

def classify_clause_rule_based(text: str) -> str:
    text_lower = text.lower()
    for category, keywords in KEYWORD_RULES.items():
        for kw in keywords:
            if kw in text_lower:
                return category
    return "Unclassified"

y_pred_baseline = X_test.apply(classify_clause_rule_based)
acc_baseline = accuracy_score(y_test, y_pred_baseline)
macro_f1_baseline = f1_score(y_test, y_pred_baseline, average="macro", zero_division=0)

logreg_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
    ("clf", LogisticRegression(random_state=42))
])
logreg_pipeline.fit(X_train, y_train)
y_pred_logreg = logreg_pipeline.predict(X_test)
acc_logreg = accuracy_score(y_test, y_pred_logreg)
macro_f1_logreg = f1_score(y_test, y_pred_logreg, average="macro", zero_division=0)

nb_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
    ("clf", MultinomialNB())
])
nb_pipeline.fit(X_train, y_train)
y_pred_nb = nb_pipeline.predict(X_test)
acc_nb = accuracy_score(y_test, y_pred_nb)
macro_f1_nb = f1_score(y_test, y_pred_nb, average="macro", zero_division=0)

svm_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
    ("clf", LinearSVC(random_state=42))
])
svm_pipeline.fit(X_train, y_train)
y_pred_svm = svm_pipeline.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
macro_f1_svm = f1_score(y_test, y_pred_svm, average="macro", zero_division=0)

results_table = pd.DataFrame({
    "Model": [
        "Rule-Based Baseline",
        "Logistic Regression",
        "Multinomial Naive Bayes",
        "Linear SVM"
    ],
    "Accuracy": [
        acc_baseline * 100,
        acc_logreg * 100,
        acc_nb * 100,
        acc_svm * 100
    ],
    "Macro F1": [
        macro_f1_baseline,
        macro_f1_logreg,
        macro_f1_nb,
        macro_f1_svm
    ]
})

print(results_table)