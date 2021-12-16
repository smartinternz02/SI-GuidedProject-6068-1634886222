

from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "mJmGY18gcbD0jth60QFAkmgKoffPvaci8SqWbVteMgqc"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask(__name__)
#model = pickle.load(open('PCA_model4.pkl', 'rb'))
@app.route('/')
def home():
    return render_template("PCA.html")
@app.route('/predict',methods=["POST","GET"])

def predict():
    input_features = [float(x) for x in request.form.values()]
    print(input_features)
    features_value = [np.array(input_features)]
    payload_scoring = {"input_data": [{"fields": ["Global_reactive_power","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"], "values": [input_features]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3e103f18-9c71-426a-86b4-325a48fd040f/predictions?version=2021-12-16', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    pred= response_scoring.json()
    print(pred)
    output=pred['predictions'][0] ['values'][0][0]
    text=round(output,2)#rounding off the decimal values to 2
    print(text)
    
    
        

    return render_template('PCA.html', prediction_text="The predicted output is:{}".format(text))
if __name__=="__main__":
    #port = int(os.getenv('PORT', 8080))
    #app.run(host='0.0.0.0', port=port, debug=False)
    app.run(debug=False)

