import numpy as np
from flask import Flask, render_template,request
import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<your API key>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


# NOTE: manually define and pass the array(s) of values to be scored in the next line

app = Flask(__name__)


@app.route("/")
def about():
    return render_template('home.html')

@app.route("/home")
def abou():
    return render_template('home.html')


 

@app.route("/predict")
def home1():
    return render_template('predict.html')

@app.route("/pred", methods=['POST','GET'])
def pred():
    Airline = request.form["Airline"]

    Source = request.form["Source"]

    Destination = request.form["Destination"]
    Date = request.form["Date"]
    Month = request.form["Month"]
    Year = request.form["Year"]

    
    DepTimeHour= request.form["Dep_Time_Hour"]
    DepTimeMins= request.form["Dep_Time_Mins"]

    Arrivaldate = request.form["Arrival_Date"]

    ArrivalTimeHour = request.form["Arrival_Time_Hour"]
    ArrivalTimeMins = request.form["Arrival_Time_Mins"]


    res= [[int(Airline), int(Source), int(Destination), int(Date), int(Month), int(Year), int(DepTimeHour), int(DepTimeMins), int(Arrivaldate), int(ArrivalTimeHour), int(ArrivalTimeMins)]]
    
    print(res)
    
    payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/643bb502-dcd0-48c2-8216-1bcf115f2462/predictions?version=2023-02-09', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    
    
    predictions = response_scoring.json()
    print(predictions)
    pred = predictions['predictions'][0]['values'][0][0]
    return render_template('submit.html', prediction_text=pred)

if __name__ == "__main__":
    app.run(debug=False)
                              