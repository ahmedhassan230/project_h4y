from fastapi import FastAPI
from dslogic_package.ml_logic import diabetes_logic
from dslogic_package.ml_logic import heart_attack_logic
from dslogic_package.ml_logic import mental_health_logic
from dslogic_package.ml_logic import osteoporosis_logic
import pandas as pd

class User():
    occupation: str
    gender: str
    days_indoors: str
    self_employed: str
    smoking: str
    alcohol_consumption: str
    sun_exposure: str
    activity: str
    dairy_intake:str
    sleeping_hrs:str
    age:int
    weight:float
    height:float


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/categorize")
def predict(usr:User):

    user_category=[]
# Convert dictionary to DataFrame
    df = pd.DataFrame.from_dict(usr, orient='index')
    # Rename columns
    df.rename(columns={'occupation': 'Occupation', 'gender': 'Sex',
                       'country': 'Country','days_indoors':'Days Indoors','self_employed':'Self Employed',
                       'smoking':'Smoking','alcohol_consumption': 'Alcohol Consumption',
                       'sun_exposure': 'Sun exposure','activity': 'Activity','dairy_intake':'Diary intake',
                       'sleeping_hrs':'Sleeping Hours','age':'Age','weight':'Weight','height':'Height'}, inplace=True)

    #calculate the BMI,BMI is weight in kilograms (kg) divided by height in meters (m) squared.
    df['BMI']= df['Weight']/df['height']**2

    #call the diabetes logic

    user_category.append(diabetes_logic.diabetes_outcome(df[['Age','BMI']]))

    #call the heart logic
    df_heart=df[['Gender','Age','Smoking','Alcohol Consumption','Sleep Hours Per Day','BMI']]
    df_heart.rename(columns={'Gender': 'Sex','Sleeping Hours':'Sleep Hours Per Day'})
    user_category.append(heart_attack_logic.hrt_attack_outcome(df_heart))

    #call the Oste logic

    #call the stress logic
