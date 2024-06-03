from fastapi import FastAPI, HTTPException
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
    #Calling models to save the model
    #diabetes_logic.diabetes_model()
    #heart_attack_logic.hrt_attack_model()

    return {"Models are saved and ready to use"}

@app.post("/categorize")

async def predict(usr:User):
    try:
        user_dict = usr.dict()
        df = pd.DataFrame([user_dict])
        user_category=[]
        # Rename columns
        df.rename(columns={'occupation': 'Occupation', 'gender': 'Sex',
                        'country': 'Country','days_indoors':'Days Indoors','self_employed':'Self Employed',
                        'smoking':'Smoking','alcohol_consumption': 'Alcohol Consumption',
                        'sun_exposure': 'Sun exposure','activity': 'Activity','dairy_intake':'Diary intake',
                        'sleeping_hrs':'Sleep Hours Per Day','age':'Age','weight':'Weight','height':'Height'}, inplace=True)
        df['BMI']= df['Weight']/df['Height']**2

        #call the diabetes logic
        diabetes_pred=diabetes_logic.diabetes_outcome(df[['Age','BMI']])
        if diabetes_pred !=None:
            user_category.append(diabetes_pred)
        #call the heartattack logic
        heart_pred=heart_attack_logic.hrt_attack_outcome(df[['Sex','Age','Smoking','Alcohol Consumption','Sleep Hours Per Day','BMI']])
        if heart_pred !=None:
            user_category.append(heart_pred)

        #call the Osteoperosis logic

        #call the Mental Health logic
        

        if user_category==[]:
            user_category.append('Generic')
        return user_category

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
