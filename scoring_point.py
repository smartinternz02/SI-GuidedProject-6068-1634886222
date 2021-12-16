# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:25:32 2021

@author: Neha reddy
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "mJmGY18gcbD0jth60QFAkmgKoffPvaci8SqWbVteMgqc"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["Global_reactive_power","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"], "values": [[12.0, 13.0, 15.0, 16.0, 17.0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3e103f18-9c71-426a-86b4-325a48fd040f/predictions?version=2021-12-16', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())