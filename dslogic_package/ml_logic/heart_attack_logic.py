import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from dslogic_package.ml_logic import registry

def hrt_attack_model():
    """
    This function is used to predict if a user can get heart attack or not
    """
    filepath='raw_data/heart_attack_prediction_dataset.csv'
    df = pd.read_csv(filepath)
    df_new=df[['Sex','Age','Smoking','Alcohol Consumption','Sleep Hours Per Day','BMI','Heart Attack Risk']]

    #encoding
    encoders = {}
    list_col = ['Sex', 'Smoking', 'Alcohol Consumption', 'Sleep Hours Per Day', 'BMI']
    for col in list_col:
        encoder = LabelEncoder()
        df_new[col] = encoder.fit_transform(df_new[col])
        encoders[col] = encoder

    y = df_new['Heart Attack Risk']
    X = df_new[['Sex', 'Age', 'Smoking', 'Alcohol Consumption', 'Sleep Hours Per Day', 'BMI']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Create and train the KNN model
    model = KNeighborsClassifier(n_neighbors=50)
    model.fit(X_train, y_train)

    #save the model
    registry.save_model(model,'heart')

def hrt_attack_outcome(X_new):

    #Preprocess X_new
    #encoding
    encoders = {}
    list_col = ['Sex', 'Smoking', 'Alcohol Consumption', 'Sleep Hours Per Day', 'BMI']
    for col in list_col:
        encoder = LabelEncoder()
        X_new[col] = encoder.fit_transform(X_new[col])
        encoders[col] = encoder


    X_new = X_new[['Sex', 'Age', 'Smoking', 'Alcohol Consumption', 'Sleep Hours Per Day', 'BMI']]

    # Standardize the data
    scaler = StandardScaler()
    X_new = scaler.fit_transform(X_new)

    #load model
    model=registry.load_model("heart")

    # Make predictions
    y_pred = model.predict(X_new)


    if float(y_pred)== 1:
        return 'heart'
    return None
