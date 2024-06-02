import pickle
from dslogic_package.params import *
import os

def save_model(model = None,logic=None):
    print(MODEL_DIR)
    model_name=f'model_{logic}.pkl'
    model_path=os.path.join(MODEL_DIR,model_name)

    #save model
    with open(model_path,'wb') as file:
        pickle.dump(model,file)
    print(model_path)
    print(f"✅  {logic} saved to Local")



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

# Adding logic to add preprocessors

def save_prep(prep = None,logic=None):
    print(PREPRO_DIR)
    prepo_name=f'prepo_{logic}.pkl'
    prepo_path=os.path.join(MODEL_DIR,prepo_name)

    #save model
    with open(prepo_path,'wb') as file:
        pickle.dump(prep,file)
    print(prepo_path)
    print(f"✅ {prepo_name} saved to Local")



def load_model(logic=None):
    """
    Return a saved model
    """
    prepo_name=f'prepo_{logic}.pkl'
    prepo_path=os.path.join(MODEL_DIR,prepo_name)

    if logic==None:
        print('Didnt receive any for logic to load a model')

    else:
        with open(prepo_path,'rb') as file:
            prep= pickle.load(file)
            print(f"✅ {prepo_name} loaded from local")

    return prep
