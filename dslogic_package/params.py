import os

LOCAL_PATH=os.path.abspath(__file__)
LOCAL_DIR=os.path.dirname(LOCAL_PATH)
MODEL_DIR=os.path.join(LOCAL_DIR,"models")
PREPRO_DIR=os.path.join(LOCAL_DIR,"ml_logic/preprocessors")
TAG_LIST=['vaccines','therapy','muscles','routine','wellbeing','selfcare','bones','fracture','pain','arthritis','cholesterol','stress','mindfulness','depression','mood','osteoporosis','challenges','lifestyle','healthy','diet','greens','wellbeing','handwashing','cleanliness','aging','vitamins','joints','health','calcium','insulin','workout','cardio','exercise','checkups','recovery','distress', 'tension','anxiety', 'fatigue', 'pressure', 'relaxation','Calm','Peaceful','Tranquil','Serene','Composed','Carefree','Easygoing','Laidback','Meditation','Yoga','Vacation','Spa','Massage','Reading','NatureWalks','Bathing','BreathingExercises','Mindfulness','Aromatherapy','Unwind','glucose','diabetes','nutrition','insulin', 'hypoglycaemia','chest pain','heartattack', 'heart','CVD', 'blood pressure', 'heart failure', 'heart attack', 'pain', 'fracture', 'back pain', 'joint pain', 'trauma', 'bone', 'bone density', 'bone loss', 'muscle pain', 'Sports', 'injury','cardiovascular diseases','IntermittentFasting','KetoDiet','Superfoods','OrganicFoods','Vegan','nutrition','worklifebalance','hygienepractices','acupuncture','minimalism']
category_tag={
        "mental_health":['depression','mood','routine','wellbeing','therapy','distress', 'tension',
'anxiety', 'fatigue', 'pressure', 'relaxation','Calm',
'Peaceful','Tranquil','Serene','Composed','Carefree','easygoing','Laidback'
'Meditation','Yoga','Vacation','Spa','massage','reading','NatureWalks','Bathing',
'BreathingExercises','Mindfulness','Aromatherapy','Unwind','health'],
        "diabetes":['glucose', 'diabetes', 'nutrition', 'insulin', 'hypoglycaemia', 'hyperglycaemia','health'],
        "heart":['cardio','chestpain', 'heart', 'CVD', 'bloodpressure', 'heartfailure', 'heartattack', 'cardiovasculardiseases','health'],
        "skeleton":['pain', 'fracture', 'backpain', 'jointpain', 'trauma', 'bone', 'bonedensity', 'boneloss', 'musclepain', 'Sports', 'injury','osteoperosis','calcium','health'],
        "generic":['routine','wellbeing','vaccines','IntermittentFasting','KetoDiet','Superfoods','OrganicFoods','Vegan','nutrition','worklifebalance','hygienepractices','acupuncture ','minimalism','challenges','lifestyle','healthy','diet','health']
    }
