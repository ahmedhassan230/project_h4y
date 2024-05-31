import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib
from dslogic_package.ml_logic import registry
import os

BASE_PATH = '/Users/admin/code/ahmedhassan230/project_h4y'
MODEL_PATH = os.path.join(BASE_PATH, 'model')

def Osteoporosis():
    df = pd.read_csv('/Users/admin/code/ahmedhassan230/project_h4y/raw_data/osteoporosis.csv')
    
    list_col = ['Body Weight', 'Calcium Intake', 'Vitamin D Intake', 'Physical Activity', 'Smoking', 'Alcohol Consumption']
    encoders = {}
    
    # Encode categorical variables
    for col in list_col:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder
    
    X = df[list_col]
    y = df['Osteoporosis']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Save the trained model, scaler, and encoders
    registry.save_model(model, 'osteoporosis')
    joblib.dump(scaler, 'scaler_osteoporosis.pkl')
    joblib.dump(encoders, 'encoders_osteoporosis.pkl')

def osteoporosis_model(X_new):
    model = registry.load_model("osteoporosis")
    scaler = joblib.load('scaler_osteoporosis.pkl')
    encoders = joblib.load('encoders_osteoporosis.pkl')
    
    # Encode new data
    for col, encoder in encoders.items():
        X_new[col] = encoder.transform(X_new[col])
    
    X_new_scaled = scaler.transform(X_new)
    
    y_pred = model.predict(X_new_scaled)
    if y_pred == 1:
        return 'osteoporosis'
    else:
        return 'no osteoporosis'
