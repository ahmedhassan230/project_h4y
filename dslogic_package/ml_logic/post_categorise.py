from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.linear_model import LogisticRegression
from dslogic_package.ml_logic import registry

nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = text.lower().strip()
    text = re.sub('[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def post_preprocessing(df):
    df['text'] = df['Content'].apply(preprocess_text)
    return df

def post_model():
    filepath = 'raw_data/fake_posts.csv'
    df = pd.read_csv(filepath)
    df.dropna(subset=['Category'], inplace=True)

    df_preprocessed = post_preprocessing(df)
    X = df_preprocessed['text']
    y = df_preprocessed['Category']

    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(X)

    lr = LogisticRegression()
    lr.fit(X_tfidf, y)

    # Save model and preprocessor
    registry.save_model(lr, 'post_categorise')
    registry.save_prep(tfidf, "tfidf_post")

def post_categorize(X_new):
    # Preprocess new data
    X_new_preprocessed = X_new.copy()
    X_new_preprocessed['Content'] = X_new_preprocessed['Content'].apply(preprocess_text)

    # Load model and preprocessor
    model = registry.load_model('post_categorise')
    tfidf = registry.load_prep("tfidf_post")

    X_post = X_new_preprocessed['Content']
    X_post_tfidf = tfidf.transform(X_post)

    # Make predictions
    y_pred = model.predict(X_post_tfidf)

    return y_pred[0]
