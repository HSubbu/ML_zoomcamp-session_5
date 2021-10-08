import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask('ChurnService')

#load dictvectorizer and model using pickle
with open('dv.bin','rb') as f1_in:
    dv = pickle.load(f1_in)

with open('model1.bin','rb') as f2_in:
    model = pickle.load(f2_in)

@app.route('/predict',methods =['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    preds = model.predict_proba(X)[:,1] #probability of note being fake
    churn = preds >0.5
    result ={
        'Churn Probability':float(preds),
        'Churn':bool(churn)

    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)