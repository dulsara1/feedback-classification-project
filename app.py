import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load('data/sentiment_model.pkl')
vectorizer = joblib.load('data/vectorizer.pkl')

# Predefined responses
responses = {
    "happiness": "Thank you! We're happy you loved our service 😊",
    "disgust": "We're sorry for the inconvenience. We'll improve this 🙏",
    "anger": "We apologize and take your feedback seriously.",
    "sadness": "We understand your concern and are here to help.",
    "fear": "Thanks for sharing your concern. We'll look into it.",
    "surprise": "Thanks for your feedback!"
}

st.title("Personalized Feedback Response System")

feedback = st.text_area("Enter user feedback")

if st.button("Analyze Feedback"):
    if feedback.strip() == "":
        st.warning("Please enter feedback")
    else:
        vec = vectorizer.transform([feedback])
        sentiment = model.predict(vec)[0]
        response = responses.get(sentiment, "Thank you for your feedback!")

        st.subheader("Predicted Sentiment")
        st.success(sentiment)

        st.subheader("Generated Response")
        st.info(response)
