import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from dslogic_package.ml_logic import registry


def Mental():
    df= pd.read_csv('/Users/admin/code/ahmedhassan230/project_h4y/raw_data/Mental Health Dataset 2.csv')


    list_col=['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country', 'Growing_Stress']
    labelencoder = LabelEncoder()
    for col in list_col:
        df[col]=labelencoder.fit_transform(df[col])
        

    # Dropping the column 'Growing_Stress'
    X = df[['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country']]

    # Define the target variable
    y = df['Growing_Stress']


    df= pd.concat([X,y], ignore_index=True, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    
    registry.save_model(model, 'osteoporosis')


def mental_model(X_new):
    
    model=registry.load_model("osteoporosis")

    list_col=['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country']
    labelencoder = LabelEncoder()
    for col in list_col:
        X_new[col]=labelencoder.fit_transform(X_new[col])
    # Make predictions
    y_pred = model.predict(X_new)

    if y_pred == 0:
        None
    else:
        return 'mental_health'
