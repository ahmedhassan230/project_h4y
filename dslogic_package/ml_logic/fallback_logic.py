def fallback(X_new):
    user_cat_dict= {"diabetic":"NO",
                        "heart":"NO",
                        "osteoporosis":"NO",
                        "mental_health":"NO",
                        "generic":"NO"}
    if X_new["gender"]=="Male" and X_new["smoking"]== 'Yes' or  X_new["alcohol_consumption"]== "Moderate" or X_new["activity"] == 'Sedentary' and X_new["age"] >50:
        user_cat_dict["heart"]="YES"
    
    if X_new["self_employed"] == 'No' and X_new["sleeping_hrs"] > 6 or X_new["smoking"]== 'Yes' or X_new["alcohol_consumption"] == "Moderate" or X_new["sun_exposure"]==' Insufficient' or X_new["activity"]== 'Sedentary':
        user_cat_dict["mental_health"]="YES"
    
    if X_new["activity"]== 'Sedentary' and X_new["weight"] > 120:
       user_cat_dict["diabetic"]="YES"
    
    return user_cat_dict