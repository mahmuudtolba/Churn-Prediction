import pickle
import numpy as np

def predict_single(customer , dv , model):
    x = dv.transform([customer])
    y_pred = model.predict_proba(x)[:,1]
    return y_pred[0]

with open('churn-model.bin', 'rb') as f_in:
    model ,dv = pickle.load(f_in)


customer = {
    'customerid': '8879-zkjof',
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'no',
    'dependents': 'no',
    'tenure': 41,
    'phoneservice': 'yes',
    'multiplelines': 'no',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'no',
    'deviceprotection': 'yes',
    'techsupport': 'yes',
    'streamingtv': 'yes',
    'streamingmovies': 'yes',
    'contract': 'one_year',
    'paperlessbilling': 'yes',
    'paymentmethod': 'bank_transfer_(automatic)',
    'monthlycharges': 79.85,
    'totalcharges': 3320.75,
    }


prediction = predict_single(customer, dv, model)
print(prediction)