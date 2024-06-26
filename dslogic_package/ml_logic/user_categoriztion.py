
import pandas as pd
from dslogic_package.ml_logic import diabetes_logic
from dslogic_package.ml_logic import heart_attack_logic
from dslogic_package.ml_logic import mental_health_logic
from dslogic_package.ml_logic import osteoporosis_logic
from dslogic_package.ml_logic import fallback_logic


def user_category(user):
    def categorize_bmi(bmi):
        if bmi < 18.5:
            return 'Underweight'
        else:
            return 'Normal'
#Declaring the return object

    user_cat_dict= {"diabetic":"NO",
                        "heart":"NO",
                        "osteoporosis":"NO",
                        "mental_health":"NO",
                        "generic":"NO"}

    user_dict = user.dict()
    df = pd.DataFrame([user_dict])
    user_category=[]

    # Rename columns
    df.rename(columns={'occupation': 'Occupation', 'gender': 'Sex',
                        'country': 'Country','days_indoors':'Days_Indoors',
                        'smoking':'Smoking','alcohol_consumption': 'Alcohol Consumption',
                        'sun_exposure': 'Vitamin D Intake','activity': 'Physical Activity','dairy_intake':'Calcium Intake',
                        'sleeping_hrs':'Sleep Hours Per Day','age':'Age','weight':'Weight','height':'Height'}, inplace=True)
    df['BMI']= df['Weight']*10000/df['Height']**2

    #Define Body Weight
    df['Body Weight'] = df['BMI'].apply(categorize_bmi)

    #call the diabetes logic
    diabetes_pred=diabetes_logic.diabetes_outcome(df[['Age','BMI']])
    if diabetes_pred !=None:
        user_category.append(diabetes_pred)
        user_cat_dict["diabetic"]="YES"

    #call the Osteoperosis logic
    #'Body Weight', 'Calcium Intake', 'Vitamin D Intake', 'Physical Activity', 'Smoking', 'Alcohol Consumption'

    osteoporosis_pred=osteoporosis_logic.osteoporosis_model(df[['Body Weight', 'Calcium Intake', 'Vitamin D Intake', 'Physical Activity', 'Smoking', 'Alcohol Consumption']])

    if osteoporosis_pred !=None:
        user_category.append(osteoporosis_pred)
        user_cat_dict["osteoporosis"]="YES"

    heart_pred=heart_attack_logic.hrt_attack_outcome(df[['Sex','Age','Smoking','Alcohol Consumption','Sleep Hours Per Day','BMI']])

    if heart_pred !=None:
        user_category.append(heart_pred)
        user_cat_dict["heart"]="YES"

    #call the Mental Health logic

    df.rename(columns={'Sex':'Gender'}, inplace = True)
    mental_health_pred=mental_health_logic.mental_model(df[['Gender', 'Occupation', 'self_employed', 'Days_Indoors', 'Country']])

    if mental_health_pred!=None:
        user_category.append(mental_health_pred)
        user_cat_dict["mental_health"]="YES"

    if user_category==[]:
        user_category.append('generic')
        user_cat_dict["generic"]="YES"

    #Fall back logic
    cat_fallback=fallback_logic.fallback(user_dict)

    if user_cat_dict['diabetic']!='YES' and cat_fallback['diabetic']=='YES':
        user_cat_dict['diabetic']='YES'

    if user_cat_dict['heart']!='YES' and cat_fallback['heart']=='YES':
        user_cat_dict['heart']='YES'

    if user_cat_dict['mental_health']!='YES' and cat_fallback['mental_health']=='YES':
        user_cat_dict['mental_health']='YES'

    return user_cat_dict
