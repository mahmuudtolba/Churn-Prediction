import pickle
import numpy as np
from flask import Flask , url_for , request , render_template , app , jsonify

with open('churn-model.bin', 'rb') as f_in:
    model ,dv = pickle.load(f_in)


def predict_single(customer , dv , model):
    x = dv.transform([customer])
    y_pred = model.predict_proba(x)[:,1]
    return y_pred[0] 

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template("main.html")

@app.route('/predict', methods = ['POST'])
def predict():
    values = [x for x in request.form.values()]
    keys = ['gender', 'seniorcitizen', 'partner', 'dependents',
     'tenure', 'phoneservice', 'multiplelines', 'internetservice',
      'onlinesecurity', 'onlinebackup', 'deviceprotection', 
      'techsupport', 'streamingtv', 'streamingmovies', 
      'contract', 'paperlessbilling', 'paymentmethod', 
      'monthlycharges', 'totalcharges']

    data = dict(zip(keys, values))
    numerical = ['tenure', 'monthlycharges', 'totalcharges']
    for feature in numerical:
        data[feature] = int(data[feature])
    output = predict_single(data , dv , model)
    return render_template("main.html",prediction_text="The Probabilty Of Churning is  {}".format(output))
    








if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)