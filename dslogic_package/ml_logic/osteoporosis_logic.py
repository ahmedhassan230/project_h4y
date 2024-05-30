import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

df= pd.read_csv('/Users/admin/code/ahmedhassan230/project_h4y/raw_data/osteoporosis.csv')

from sklearn.preprocessing import LabelEncoder
list_col=['Body Weight', 'Calcium Intake', 'Vitamin D Intake', 'Physical Activity', 'Smoking', 'Alcohol Consumption']
labelencoder = LabelEncoder()
for col in list_col:
    df[col]=labelencoder.fit_transform(df[col])
    
X=df[['Body Weight', 'Calcium Intake', 'Vitamin D Intake', 'Physical Activity', 'Smoking', 'Alcohol Consumption']]
y=df['Osteoporosis']

df=pd.concat([X,y], axis=1, ignore_index= True)
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

model= LogisticRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)

return y_pred