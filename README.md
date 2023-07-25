## End to End Machine Learning Project to predict customers churn 

* I created an app to determine Telecom Churn based on various customer factors like Monthly Data Usae / Monthly bills or whether the customer opted for Premium TV / Movies etc.
* Imputed missing values, handled categorical features etc to develop a Classification Model to predict churn
* Optimized differet classifications like Random Forest, Decision Tree, Logistic Classification, Artificial Neural Network (ANN) with a Precision of 60%
* Built a client facing API using flask (CLient/End-User can use Front End UI) and/or shared drive location to put their test data

## Code and Resources Used
* Python Version: 3.11
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* For Web Framework Requirements: pip install -r requirements.txt

## Data Ingestion
* Client can use a Front End website to enter customer data to predict churn
* Client can also use a shared drive location to put the raw bulk data. The Machine Learning Pipeline would automatically run the pre-processing tasks and give the ouput in a shared location.

## Data Validation
* I used python scripts to validate the raw data sent by client.
* This is done by verifying the __Name of File__ and __Number of Columns__ in the file. More such checks can be added if needed
* Data that doesn't pass the validation check goes to __folder__ : bad_data_archived , while data that passes all checks goes to __folder__ : good_data

## Data Logging and Custom Exception handling
* Every step is logged and a separate folder is created for logging. Such process can help identify problems in the code
* Every error is logged in the logger file with a Custom Error Handling exception message

## Data Pre-Processing
Following steps were taken to clean the data
* Correcting the column headers
* Using sklearn Simple Imputer to impute missing values using strategies like Mean / Median / Mode
* Removing special characters from all columns
* Using Chi2 square for Categorical Columns to select relevant features and ignore redundant ones
* Using Mutual Info Gain for Numerical Columns to select relevant features and ignore redundant ones

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights

## Model Training

## Front End API
![Prediction_1](https://github.com/SrijanDeo-DA-DS/DS_Predict_TelecomChurn/assets/88278620/8bc85776-7933-4e41-9c09-54a57834dce1)
![Prediction_0](https://github.com/SrijanDeo-DA-DS/DS_Predict_TelecomChurn/assets/88278620/d88bb688-0d0e-4cc8-95ff-c91bf863a4c5)


## Productionize the model
Coming soon...
