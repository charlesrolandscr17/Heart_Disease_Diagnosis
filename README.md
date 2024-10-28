# Heart Disease Diagnosis

## Project Overview

This project aims to diagnose heart disease using a machine learning model. Initially approached as a classification task, the project was adapted to a regression model to provide a likelihood percentage of heart disease based on user input.

## Model Description

The model is built using TensorFlow and follows a regression approach. It outputs a probability score indicating the likelihood of a user having heart disease.

## Steps Taken

1. **Import Libraries and Load Data**: Imported the necessary libraries and read the dataset.
2. **Data Examination**: Analyzed the dataset, which appeared well-pruned and preprocessed, requiring no additional preprocessing steps.
3. **Data Splitting**: Split the data into feature variables and target variables.
4. **Train-Test Split**: Used Scikit-learn to split the data into training and testing sets with an 80/20 ratio.
5. **ModelCheckpoint Setup**: Configured a `ModelCheckpoint` callback to save the best model during training based on validation loss.
6. **Model Architecture**: Created a Sequential model with three Dense layers, with the middle layer utilizing the ReLU activation function.
7. **Model Compilation**: Compiled the model with Mean Absolute Error as the loss function, Adam as the optimizer, and Mean Absolute Error as a metric.
8. **Model Training**: Trained the model on the training data and validated it with the test data over 100 epochs.

## Running the Application

To run the application locally, follow these steps:

1. **Create a Virtual Environment**: Use a virtual environment tool of your choice. Below is an example using `virtualenv`:
   ```bash
   virtualenv venv
   ```

2. **Install Required Packages**: Install the necessary packages by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Streamlit Server**: Run the following command to start the application:
   ```bash
   streamlit run app.py
   ```

## Live Demo

The app is hosted on Streamlit and can be accessed via the following link:

[Heart Disease Diagnosis App](https://heart-disease-diagnosis.streamlit.app/)

## Conclusion

This project effectively utilizes a regression model to predict the likelihood of heart disease. By following the outlined steps, you can replicate the setup and run the application locally or access the live demo for predictions based on user input.
