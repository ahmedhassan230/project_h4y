import nltk
import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import random
from dslogic_package.params import *
from dslogic_package.ml_logic import post_categorise

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def random_tags(category,tag_list_final):
    print("entering random tag generation")
    print(str(category))
    n_items=5-len(tag_list_final)
    if n_items>0:
        tags_not_currently_present= [tag for tag in category_tag[category] if tag not in tag_list_final]
        temp= random.sample(tags_not_currently_present, n_items)
        print(temp)
        tag_list_final=temp+tag_list_final
    return tag_list_final


# Preprocess the text
def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text

def extract_keywords(text, num_keywords=10):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]

    # Get top n keywords based on TF-IDF scores
    sorted_indices = tfidf_scores.argsort()[::-1]
    top_keywords = [feature_names[idx] for idx in sorted_indices[:num_keywords]]
    return top_keywords
def tags(keywords, entities):
    return list(set(keywords + entities))

def extract_entities(text):
    doc = nlp(text)
    entities = [entity.text for entity in doc.ents if entity.label_ in ['PERSON', 'ORG', 'GPE', 'DATE', 'TIME', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']]
    return entities

def health_specific_tags(tags):
    t=TAG_LIST
    t_lower=[tag.lower() for tag in t]
    tag_list_new= [tag for tag in tags if tag in t ]
    return tag_list_new

def create_tag(text):
    text_preprocessed=preprocess_text(text)
    keywords=extract_keywords(text_preprocessed)
    entities=extract_entities(text_preprocessed)
    tag_list_new=tags(keywords, entities)
    tag_list_final=health_specific_tags(tag_list_new)
    post_df = pd.DataFrame([{'Content':text}])
    category=post_categorise.post_categorize(post_df)
    tag_list_final_random=random_tags(str(category),tag_list_final)
    return tag_list_final_random
