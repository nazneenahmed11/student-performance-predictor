import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# ---- Load data and model ----
df = pd.read_csv("StudentsPerformance.csv")

df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
if "passed" not in df.columns:
    df["passed"] = (df["average_score"] >= 60).astype(int)

rf_model = joblib.load("rf_model.joblib")

# ---- Optional light styling for prediction card ----
st.markdown("""
<style>
.prediction-card {
    background-color: #F9FAFB;
    padding: 1.5rem;
    border-radius: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Student Performance Predictor")

# ---- Tabs ----
tab1, tab2 = st.tabs(["Overview", "Prediction"])

# ========= TAB 1: OVERVIEW =========
with tab1:
    # Summary cards
    pass_rate = (df["passed"].mean() * 100).round(1)
    overall_avg = df["average_score"].mean().round(1)
    total_students = len(df)

    st.subheader("Overall summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Pass rate ✅", f"{pass_rate}%")
    col2.metric("Avg score 🎯", f"{overall_avg}")
    col3.metric("Students 👥", f"{total_students}")

    st.write("Use the sidebar filters to explore performance across groups.")

    # Filters + chart
    st.sidebar.header("Filters")
    gender_filter = st.sidebar.multiselect(
        "Gender",
        options=df["gender"].unique(),
        default=list(df["gender"].unique()),
    )
    prep_filter = st.sidebar.multiselect(
        "Prep course",
        options=df["test preparation course"].unique(),
        default=list(df["test preparation course"].unique()),
    )

    filtered_df = df[
        df["gender"].isin(gender_filter)
        & df["test preparation course"].isin(prep_filter)
    ]

    st.subheader("Average score by prep course")
    grouped = (
        filtered_df
        .groupby("test preparation course")["average_score"]
        .mean()
        .reset_index()
    )
    st.bar_chart(grouped.set_index("test preparation course"))

# ========= TAB 2: PREDICTION =========
with tab2:
    st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

    st.subheader("Custom prediction")
    st.write("Set the scores to generate a prediction and risk level for one student.")

    # Sliders + number inputs
    col_m1, col_m2 = st.columns([3, 1])
    with col_m1:
        math = st.slider("Math score", 0, 100, 70, key="math_slider")
    with col_m2:
        math = st.number_input(" ", 0, 100, value=math, key="math_number")

    col_r1, col_r2 = st.columns([3, 1])
    with col_r1:
        reading = st.slider("Reading score", 0, 100, 70, key="read_slider")
    with col_r2:
        reading = st.number_input("  ", 0, 100, value=reading, key="read_number")

    col_w1, col_w2 = st.columns([3, 1])
    with col_w1:
        writing = st.slider("Writing score", 0, 100, 70, key="write_slider")
    with col_w2:
        writing = st.number_input("   ", 0, 100, value=writing, key="write_number")

    if st.button("Predict"):
        input_df = pd.DataFrame({
            "math score": [math],
            "reading score": [reading],
            "writing score": [writing],
        })

        pred = rf_model.predict(input_df)[0]
        result = "Pass ✅" if pred == 1 else "Fail ❌"

        avg = (math + reading + writing) / 3

        # Risk label
        if avg < 50:
            risk = "High risk 🔴 – strong support needed"
        elif avg < 60:
            risk = "Medium risk 🟠 – monitor and support"
        else:
            risk = "Low risk 🟢 – likely to pass"

        st.success(f"Model prediction: {result}")

        if avg >= 60:
            st.markdown(f"**Average score:** :green[{avg:.1f}]")
        else:
            st.markdown(f"**Average score:** :red[{avg:.1f}]")

        st.write(f"Risk level: **{risk}**")

        st.caption(
            "Note: The green/red average uses a fixed 60% rule; "
            "the model prediction is based on patterns learned from data."
        )

        # Bar chart inside expander (toggle)
        with st.expander("📈 Show subject‑wise scores"):
            scores_df = pd.DataFrame({
                "subject": ["Math", "Reading", "Writing"],
                "score": [math, reading, writing],
            })
            st.bar_chart(scores_df.set_index("subject"))

    st.markdown("</div>", unsafe_allow_html=True)
