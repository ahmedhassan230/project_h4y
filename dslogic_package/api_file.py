from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dslogic_package.ml_logic import user_categoriztion
from dslogic_package.ml_logic import recommend_posts
import pandas as pd


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
    country:str


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
        return user_categoriztion.user_category(usr)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#Adding Logic to return the Posts

@app.post("/posts")
async def post_recommendation(usr:User):
    try:
        user_category= user_categoriztion.user_category(usr)
        return recommend_posts.post_finder(user_category)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
