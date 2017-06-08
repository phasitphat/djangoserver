import pickle
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import cross_val_score

def loadForest():
    loaded_forest = pickle.load(open('predict_pickle.sav', 'rb'))
    return loaded_forest;