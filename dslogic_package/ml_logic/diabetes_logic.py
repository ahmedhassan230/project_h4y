
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from dslogic_package.ml_logic import registry

def diabetes_model():
    """
    This function is used to predict if a user is diabetic or not
    """
    #NEED TO FIND A WAY STORE THE DATASET REMOTELY
    filepath='raw_data/diabetes.csv'
    df = pd.read_csv(filepath)
    y = df['Outcome']
    X= df[['Age','BMI']]
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    #X = scaler.transform(X)
   # X_test = scaler.transform(X_test)

    # Create and train the KNN  model
    model = KNeighborsClassifier(n_neighbors=10)
    model.fit(X, y)

    #save the model
    registry.save_model(model,'diabetes')




def diabetes_outcome(X_new):
    #load model
    model=registry.load_model('diabetes')
    # Make predictions
    y_pred = model.predict(X_new)
    #y_prob = model.predict_proba(X_test)[:, 1]

    if float(y_pred)== 1:
        return 'diabetic'

    return None
