# Iris Flower Classification

Streamlit app for predicting an Iris species from sepal and petal measurements.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run iris_app.py
```

The app expects `iris_model.pkl` in the repository root. Existing model artifacts are preserved. Pickled scikit-learn models can be version-sensitive; use the training version if loading fails.
