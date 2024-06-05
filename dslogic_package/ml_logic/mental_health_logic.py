import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import joblib
from dslogic_package.ml_logic import registry
from dslogic_package.params import *

# Define the base path and model path
BASE_PATH = '/Users/admin/code/ahmedhassan230/project_h4y'
#MODEL_PATH = os.path.join(BASE_PATH, 'models')
#DATA_PATH = os.path.join(BASE_PATH, 'raw_data', 'Mental Health Dataset 2.csv')

def Mental():
    df = pd.read_csv('/Users/admin/code/ahmedhassan230/project_h4y/raw_data/Mental Health Dataset 2.csv')

    list_col = ['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country']
    encoders = {}

    # Encode categorical variables
    for col in list_col:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder

    # Define features and target
    X = df[['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country']]
    y = df['Growing_Stress']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train the model
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)


    registry.save_model(model, 'mental')
    scaler_path=os.path.join(PREPRO_DIR,"scaler_mental.pkl")
    encoder_path=os.path.join(PREPRO_DIR,"encoders_mental.pkl")
    joblib.dump(scaler, scaler_path)
    joblib.dump(encoders,encoder_path)

def mental_model(X_new):


    scaler_path=os.path.join(PREPRO_DIR,"scaler_mental.pkl")
    encoder_path=os.path.join(PREPRO_DIR,"encoders_mental.pkl")

    model = registry.load_model("mental")
    scaler = joblib.load(scaler_path)
    encoders = joblib.load(encoder_path)

    # Ensure X_new has the correct format
    required_columns = ['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country']
    if not all(col in X_new.columns for col in required_columns):
        raise ValueError(f"Input data must contain the following columns: {required_columns}")

    # Encode new data
    for col, encoder in encoders.items():
        X_new[col] = encoder.transform(X_new[col])

    # Scale new data
    X_new_scaled = scaler.transform(X_new)

    # Make predictions
    y_pred = model.predict(X_new_scaled)
    print("MENTAL MODEL IS DONE")
    
    if y_pred == 0:
        return None
    else:
        return 'mental_health'
