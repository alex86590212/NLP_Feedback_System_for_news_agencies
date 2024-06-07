import pandas as pd
from transformers import pipeline
from keybert import KeyBERT
import os

data_file = r'file_directory'
output_file = r'file_directory'

# Define candidate labels
candidate_labels = [
    'Positive Feedback',
    'Negative Feedback',
    'Suggestion'
]


zero_shot_classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


kw_model = KeyBERT()


additional_keywords = {
    'Sport': ['sport'],
    'Economics': ['economics'],
    'Politics': ['politics']
}

def add_feedback(feedback):
    if os.path.exists(data_file):
        df = pd.read_csv(data_file)
    else:
        df = pd.DataFrame(columns=['Feedback'])

   
    new_feedback = pd.DataFrame({'Feedback': [feedback]})
    df = pd.concat([df, new_feedback], ignore_index=True)
    df.to_csv(data_file, index=False)

def process_feedback():
    df = pd.read_csv(data_file)

    
    df['Predicted Category'] = df['Feedback'].apply(zero_shot_classify)

    
    df['Keywords'] = df['Feedback'].apply(extract_keywords)

    
    df['Additional Category'] = df['Keywords'].apply(classify_additional_keywords)

    
    improvable_feedback = df[df['Predicted Category'] == 'Suggestion']
    improvable_feedback.to_csv(output_file, index=False)

def zero_shot_classify(feedback):
    prediction = zero_shot_classifier(feedback, candidate_labels=candidate_labels)
    print(f"Feedback: {feedback}")
    print(f"Prediction: {prediction}")
    return prediction['labels'][0]

def extract_keywords(feedback):
    keywords = kw_model.extract_keywords(feedback, keyphrase_ngram_range=(1, 2), stop_words='english')
    return [kw[0] for kw in keywords]

def classify_additional_keywords(keywords):
    for category, keyword_list in additional_keywords.items():
        for keyword in keywords:
            if any(k in keyword.lower() for k in keyword_list):
                return category
    return 'Other'
