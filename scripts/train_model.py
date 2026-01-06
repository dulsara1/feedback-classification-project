import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib  # for saving the model

# 1. Load train and test data
X_train = pd.read_csv('../data/X_train.csv')['feedback_text']
X_test = pd.read_csv('../data/X_test.csv')['feedback_text']
y_train = pd.read_csv('../data/y_train.csv')['sentiment']
y_test = pd.read_csv('../data/y_test.csv')['sentiment']

# 2. Convert text to TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 3. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# 4. Evaluate model
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 5. Save the model and vectorizer for later use
joblib.dump(model, '../data/sentiment_model.pkl')
joblib.dump(vectorizer, '../data/vectorizer.pkl')

print("Model and vectorizer saved successfully!")
