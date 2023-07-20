from flask import Flask, render_template, request
import jsonify
import requests
import pickle
#import numpy as np
import sklearn
import pandas as pd
#from sklearn.preprocessing import StandardScaler
#from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)
model = pickle.load(open('random_forest_classification_model.pkl', 'rb'))
## Route for a home page

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html') 

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        Unlimited_Data=request.form['Unlimited_Data']
        if Unlimited_Data == 'Yes':
            Unlimited_Data = 1
        else:
            Unlimited_Data = 0
        Streaming_TV=request.form['Streaming_TV']
        if Streaming_TV == 'Yes':
            Streaming_TV = 1
        else:
            Streaming_TV = 0
        Streaming_Music=request.form['Streaming_Music']
        if Streaming_Music == 'Yes':
            Streaming_Music = 1
        else:
            Streaming_Music = 0
        Streaming_Movies=request.form['Streaming_Movies']
        if Streaming_Movies == 'Yes':
            Streaming_Movies = 1
        else:
            Streaming_Movies = 0
        Premium_Tech_Support=request.form['Premium_Tech_Support']
        if Premium_Tech_Support == 'Yes':
            Premium_Tech_Support = 1
        else:
            Premium_Tech_Support = 0
        Number_of_Referrals=int(request.form['Number_of_Referrals'])
        Tenure_in_Months=int(request.form['Tenure_in_Months'])
        Total_Charges=int(request.form['Total_Charges'])
        Monthly_Charge=int(request.form['Monthly_Charge'])
        Total_Long_Distance_Charges=int(request.form['Total_Long_Distance_Charges'])
        
        prediction=model.predict([[Unlimited_Data,Streaming_TV,Streaming_Music,Streaming_Movies,Premium_Tech_Support,Number_of_Referrals,Tenure_in_Months,Total_Charges,Monthly_Charge,Total_Long_Distance_Charges]])
        output=round(prediction[0],2)
        return render_template('home.html',results = output)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True, use_reloader=False, port=0000)      
