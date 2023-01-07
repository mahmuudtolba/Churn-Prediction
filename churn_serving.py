import pickle
import numpy as np

def predict_single(customer , dv , model):
    x = dv.transform([customer])
    y_pred = model.predict_prba(x)[:,1]
    return y_pred[0]