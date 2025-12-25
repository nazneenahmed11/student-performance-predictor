import joblib
import pandas as pd
import streamlit as st

rf_model = joblib.load("rf_model.joblib")

st.title("Student Performance Predictor")
st.write("Enter exam scores to see the prediction.")

math = st.slider("Math score", 0, 100, 70)
reading = st.slider("Reading score", 0, 100, 70)
writing = st.slider("Writing score", 0, 100, 70)

if st.button("Predict"):
    input_df = pd.DataFrame({
        'math score': [math],
        'reading score': [reading],
        'writing score': [writing]
    })

    pred = rf_model.predict(input_df)[0]   # 0 or 1 from your RF
    result = "Pass ✅" if pred == 1 else "Fail ❌"

    avg = (math + reading + writing) / 3

    if avg >= 60:
        st.markdown(f"**Average score:** :green[{avg:.1f}]")
    else:
        st.markdown(f"**Average score:** :red[{avg:.1f}]")

    st.success(f"Model prediction: {result}")
    st.caption(
        "Note: The green/red average uses a fixed 60% rule; "
        "the model prediction is based on patterns learned from data."
    )

    


