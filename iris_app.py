# -*- coding: utf-8 -*-
"""Streamlit interface for Iris species classification."""

import joblib
import numpy as np
import streamlit as st


@st.cache_resource
def load_model():
    """Load the trained classifier once per Streamlit session."""
    return joblib.load("iris_model.pkl")


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


st.title("Md Luqman Ali — Iris Species Prediction")
st.markdown("Predict an Iris species from sepal and petal measurements.")

sepal_length = st.number_input("Sepal length (cm)", min_value=0.1, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal width (cm)", min_value=0.1, max_value=10.0, value=3.0)
petal_length = st.number_input("Petal length (cm)", min_value=0.1, max_value=10.0, value=1.5)
petal_width = st.number_input("Petal width (cm)", min_value=0.1, max_value=10.0, value=0.2)

if st.button("Predict"):
    try:
        features = validate_measurements(
            [sepal_length, sepal_width, petal_length, petal_width]
        )
        prediction = load_model().predict(features)[0]
        st.success(f"Predicted species: {prediction}")
    except (OSError, ValueError, AttributeError) as exc:
        st.error(f"Prediction could not be completed: {exc}")
