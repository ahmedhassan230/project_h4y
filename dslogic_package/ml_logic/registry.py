import pickle
from dslogic_package.params import *
import os

def save_model(model = None,logic=None):

    model_name=f'model_{logic}.pkl'
    model_path=os.path.join(MODEL_DIR,model_name)

    #save model
    with open(model_path,'wb') as file:
        pickle.dump(model,file)

    print("✅ Model saved to Local")



def load_model(logic=None):
    """
    Return a saved model
    """


    model_name=f'model_{logic}.pkl'
    model_path=os.path.join(MODEL_DIR,model_name)

    if logic==None:
        print('Didnt receive any for logic to load a model')

    else:
        with open(model_path,'rb') as file:
            model= pickle.load(file)
            print(f"✅ {logic} Model loaded from local")

    return model
