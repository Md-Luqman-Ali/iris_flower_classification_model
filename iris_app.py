# -*- coding: utf-8 -*-
"""Streamlit interface for Iris species classification."""

from pathlib import Path

import joblib
import numpy as np
import streamlit as st

MODEL_PATH = Path(__file__).with_name("iris_model.pkl")


@st.cache_resource
def load_model():
    """Load the trained classifier once per Streamlit process."""
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"Model artifact not found: {MODEL_PATH.name}")
    return joblib.load(MODEL_PATH)


def validate_measurements(values):
    """Validate four positive, finite Iris measurements."""
    values = np.asarray(values, dtype=float)
    if values.shape != (4,):
        raise ValueError("Exactly four measurements are required.")
    if not np.all(np.isfinite(values)):
        raise ValueError("Measurements must be finite numbers.")
    if np.any(values <= 0):
        raise ValueError("Measurements must be greater than zero.")
    return values.reshape(1, -1)


st.set_page_config(page_title="Iris Classifier | Portfolio", page_icon="🌸", layout="centered")
st.title("Iris Flower Classification")
st.caption("Machine learning demo · scikit-learn · Streamlit")
st.write("Enter sepal and petal measurements in centimetres to predict the Iris species.")

with st.expander("Try a sample input"):
    st.code("Setosa: 5.1, 3.5, 1.4, 0.2\nVersicolor: 6.0, 2.9, 4.5, 1.5\nVirginica: 6.5, 3.0, 5.2, 2.0")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal length (cm)", min_value=0.1, max_value=10.0, value=5.1, step=0.1)
    petal_length = st.number_input("Petal length (cm)", min_value=0.1, max_value=10.0, value=1.4, step=0.1)
with col2:
    sepal_width = st.number_input("Sepal width (cm)", min_value=0.1, max_value=10.0, value=3.5, step=0.1)
    petal_width = st.number_input("Petal width (cm)", min_value=0.1, max_value=10.0, value=0.2, step=0.1)

if st.button("Predict species", type="primary", use_container_width=True):
    try:
        features = validate_measurements([sepal_length, sepal_width, petal_length, petal_width])
        model = load_model()
        prediction = model.predict(features)[0]
        st.success(f"Predicted species: **{prediction}**")
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(features)[0]
            labels = getattr(model, "classes_", range(len(probabilities)))
            st.subheader("Class probabilities")
            st.bar_chart({str(label): float(prob) for label, prob in zip(labels, probabilities)})
    except (OSError, ValueError, AttributeError, TypeError) as exc:
        st.error(f"Prediction could not be completed: {exc}")

st.divider()
st.caption("Portfolio demonstration only. Predictions depend on the supplied model artifact and its training environment.")
