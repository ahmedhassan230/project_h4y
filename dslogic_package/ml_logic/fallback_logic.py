def fallback(X_new):
    user_cat_dict= {"diabetic":"NO",
                        "heart":"NO",
                        "osteoporosis":"NO",
                        "mental_health":"NO",
                        "generic":"NO"}
    if (X_new["Gender"]=="Male") and X_new["Smoking"]== 'Yes' or  X_new["Alcohol Consumption"]== "Moderate" or X_new["Physical Activity"] == 'Sedentary' and X_new["Age"] >50:
        user_cat_dict["heart"]="YES"

    if (X_new["self_employed"] == 'No') and X_new["Sleep Hours Per Day"] > 6 or X_new["Smoking"]== 'Yes' or X_new["Alcohol Consumption"] == "Moderate" or X_new["Vitamin D Intake"]==' Insufficient' or X_new["Physical Activity"]== 'Sedentary':
        user_cat_dict["mental_health"]="YES"

    if (X_new["Physical Activity"]== 'Sedentary') and X_new["Weight"] > 120:
       user_cat_dict["diabetic"]="YES"

    return user_cat_dict
