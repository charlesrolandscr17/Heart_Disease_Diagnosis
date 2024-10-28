import streamlit as st
import numpy as np
import tensorflow as tf

st.title("Heart Disease Diagnosis")

ckpt_dir = "model/checkpoint.model.keras"

model_0 = tf.keras.models.load_model(ckpt_dir)


def inference(data):
    input_data = np.array(data)

    reshaped_input = np.expand_dims(input_data, axis=0)

    return model_0(reshaped_input).numpy()


# age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target

with st.form("my_form"):
    st.markdown("# Data Form")
    age = st.number_input("Age", min_value=0)
    sex = st.number_input("Sex", min_value=0, max_value=1)
    cp = st.number_input("cp", min_value=0)
    trestbps = st.number_input("Trestbps", min_value=0)
    chol = st.number_input("Chol", min_value=0)
    fbs = st.number_input("fbs", min_value=0)
    restecg = st.number_input("Restecg", min_value=0)
    thalach = st.number_input("Thalach", min_value=0)
    exang = st.number_input("Exang", min_value=0)
    oldpeak = st.number_input("Oldpeak", step=0.1)
    slope = st.number_input("Slope", min_value=0)
    ca = st.number_input("CA", min_value=0)
    thal = st.number_input("Thal", min_value=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        data = [
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
        ]

        result = inference(data)

        st.write(
            f"You have a {result[0][0]*100:.2f}% likelihood of having heart disease"
        )
