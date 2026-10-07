import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.title("Contract Clause Classification Tool")
st.write("Enter a legal clause below to predict its category.")

df = pd.read_csv("contract_clauses_1200.csv")

vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
X = vectorizer.fit_transform(df["text"])
y = df["category"]

model = LogisticRegression(random_state=42)
model.fit(X, y)

user_text = st.text_area("Clause Text:", height=120)

if st.button("Classify"):
    if user_text.strip() != "":
        text_vec = vectorizer.transform([user_text])
        prediction = model.predict(text_vec)[0]
        probabilities = model.predict_proba(text_vec)[0]
        
        st.subheader("Prediction: " + prediction)
        
        st.write("Confidence Scores:")
        for category, prob in zip(model.classes_, probabilities):
            st.write(f"{category}: {prob * 100:.2f}%")
    else:
        st.write("Please enter some text first.")