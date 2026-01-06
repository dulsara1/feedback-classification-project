import pandas as pd
import joblib

# 1. Load trained model and vectorizer
model = joblib.load('../data/sentiment_model.pkl')
vectorizer = joblib.load('../data/vectorizer.pkl')

# 2. Example new feedbacks
new_feedback = [
    "The app is very slow and keeps crashing.",
    "Excellent service, very happy with the support!"
]

# 3. Convert text to TF-IDF features
new_feedback_vec = vectorizer.transform(new_feedback)

# 4. Predict sentiment
predictions = model.predict(new_feedback_vec)

# 5. Show results
for text, pred in zip(new_feedback, predictions):
    print(f"Feedback: {text}\nPredicted Sentiment: {pred}\n")
