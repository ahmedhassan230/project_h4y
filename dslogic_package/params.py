import os

LOCAL_PATH=os.path.abspath(__file__)
LOCAL_DIR=os.path.dirname(LOCAL_PATH)
MODEL_DIR=os.path.join(LOCAL_DIR,"models")
PREPRO_DIR=os.path.join(LOCAL_DIR,"ml_logic/preprocessors")
TAG_LIST=["Anxiety", "Stress", "Depression", "Mindfulness", "Wellness", "Mental Health Therapy", "Resilience", "Self-care", "Psychology", "Happiness", "Diabetes Prevention", "Glucose", "Insulin", "Diet", "Glycemic", "Fitness", "Foot Care", "Type 1 Diabetes", "Type 2 Diabetes", "Cardio", "Heart Diet", "Cholesterol", "Blood Pressure", "Heart Care", "Physical Rehab", "Stress", "Surgery", "Heart Rate", "Heart Health", "Density", "Calcium", "Osteoporosis", "Joints", "Arthritis", "Fracture", "Vitamins", "Physical Therapy", "Aging", "Bone Health", "Nutrition", "Exercise", "Checkups", "Hydration", "Sleep", "Weight", "Seasonal", "Prevention", "Vaccines", "Health"]
category_tag={
        "mental_health":["Anxiety", "Stress", "Depression", "Mindfulness", "Wellness", "Mental Health Therapy", "Resilience", "Self-care", "Psychology", "Happiness"],
        "diabetes":["Glucose", "Insulin", "Diet", "Glycemic", "Fitness", "Foot Care", "Type 1 Diabetes", "Type 2 Diabetes"],
        "heart":["Cardio", "Heart Diet", "Cholesterol", "Blood Pressure", "Heart Care", "Physical Rehab", "Stress", "Surgery", "Heart Rate", "Heart Health"],
        "skeleton":["Density", "Calcium", "Osteoporosis", "Joints", "Arthritis", "Fracture", "Vitamins", "Physical Therapy", "Aging", "Bone Health"],
        "generic":["Nutrition", "Exercise", "Checkups", "Hydration", "Sleep", "Weight", "Seasonal", "Prevention", "Vaccines", "Health","Mindfulness", "Wellness","Resilience", "Self-care", "Psychology", "Happiness"]
    }
