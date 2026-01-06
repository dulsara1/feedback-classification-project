import pandas as pd
import joblib
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

# Load trained model and vectorizer
model = joblib.load('data/sentiment_model.pkl')
vectorizer = joblib.load('data/vectorizer.pkl')

# Response templates
responses = {
    "happiness": "Thank you for your positive feedback!",
    "disgust": "We are sorry for the inconvenience.",
    "anger": "We sincerely apologize.",
    "sadness": "We understand your concern.",
    "fear": "Thank you for sharing your concern.",
    "surprise": "Thank you for your feedback!"
}

# Load evaluation data
df = pd.read_csv('evaluation_samples.csv')

bleu_scores = []
rouge_scores = []

scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

for _, row in df.iterrows():
    vec = vectorizer.transform([row['user_feedback']])
    sentiment = model.predict(vec)[0]
    generated = responses.get(sentiment, "Thank you.")

    reference = row['reference_response'].split()
    candidate = generated.split()

    bleu_scores.append(sentence_bleu([reference], candidate))
    rouge_scores.append(
        scorer.score(row['reference_response'], generated)['rougeL'].fmeasure
    )

print("Average BLEU Score:", sum(bleu_scores) / len(bleu_scores))
print("Average ROUGE-L Score:", sum(rouge_scores) / len(rouge_scores))
