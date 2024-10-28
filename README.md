# Heart_Disease_Diagnosis

## Model Description

The model is trained using tensorflow. The project appeared to be a classification project based on the target. However, based on the requirement "When the form is submitted, pass the data to the model and display the
prediction result (e.g., “You have a 70% likelihood of having heart disease”)", the only way to satusfy it is to train a regression model.

### Steps Taken
1. Imported the required libraries and read in the data.
2. Examined the data. The data looked well pruned and preprocessed and did not require more preprocessing.
3. The data was slit between the Feature variables and the Target variables.
4. Using scikitlearn, the data was then split into the train and test split with a ratio of 80/20.
5. I then instatiated a ModelCheckpoint callback to save the best model during training based on the validation loss.
6. I instantiated a Sequential model with 3 Dense layers with the middle layer having a relu activation.
7. The model was then compiled with a loss of Mean Absolute Error, Adam optimizer, and Mean Absolute Error as one of the metrics.
8. The model is then trained with the training data, validated with the test data for 100 epochs.

## Run the Application

1. Create a virtual environment using a library of your choice, such as uv, virtualenv, conda among others. The example below uses uv.
`uv venv`

2. Install the required packages.
`pip install -r requirements.txt`

3. Run streamlit to start up the servers

`streamlit run app.py`
