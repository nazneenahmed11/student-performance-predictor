import streamlit as st
import pandas as pd

st.title("Student Performance Predictor")
st.write("Enter exam scores to see the prepared input (model hook will be added later).")

math = st.number_input("Math score", 0, 100, 70)
reading = st.number_input("Reading score", 0, 100, 70)
writing = st.number_input("Writing score", 0, 100, 70)

if st.button("Show prepared input"):
    df = pd.DataFrame([{
        "math score": math,
        "reading score": reading,
        "writing score": writing
    }])
    st.success("Prepared input row:")
    st.write(df)
