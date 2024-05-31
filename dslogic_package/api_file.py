from fastapi import FastAPI
from dslogic_package.ml_logic import diabetes_logic
from dslogic_package.ml_logic import heart_attack_logic
from pydantic import BaseModel
#from dslogic_package.ml_logic import mental_health_logic
#from dslogic_package.ml_logic import osteoporosis_logic
import pandas as pd
from dataclasses import dataclass, asdict

class User(BaseModel):
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

@app.post("/validate")
def validate():

    user_category=[]
# Convert dictionary to DataFrame

@app.post("/categorize")

async def predict(usr:User):
    user_dict = usr.dict()
    df = pd.DataFrame([user_dict])
    user_category=[]
        # Rename columns
    df.rename(columns={'occupation': 'Occupation', 'gender': 'Sex',
                       'country': 'Country','days_indoors':'Days Indoors','self_employed':'Self Employed',
                       'smoking':'Smoking','alcohol_consumption': 'Alcohol Consumption',
                       'sun_exposure': 'Sun exposure','activity': 'Activity','dairy_intake':'Diary intake',
                       'sleeping_hrs':'Sleeping Hours','age':'Age','weight':'Weight','height':'Height'}, inplace=True)
    df['BMI']= df['Weight']/df['Height']**2
    #call the diabetes logic

    user_category.append(diabetes_logic.diabetes_outcome(df[['Age','BMI']]))

    return user_category
