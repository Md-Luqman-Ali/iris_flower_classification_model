# Iris Flower Classification

An interactive Streamlit application that predicts an Iris species from four flower measurements. The model is loaded from the repository's existing `iris_model.pkl` artifact.

## Live demo

After deployment, add the public Streamlit Community Cloud URL here. A demo link is intentionally not listed until a deployment has been verified.

## Run locally

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Windows cmd: .venv\\Scripts\\activate.bat
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run iris_app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Sign in at https://share.streamlit.io/ and connect GitHub.
3. Create an app from this repository and select `iris_app.py` as the main file.
4. Deploy. Keep `iris_model.pkl` in the repository root; the app resolves the artifact relative to its own file.
5. Open the generated public URL and test a sample input.

## Model and limitations

- Inputs: sepal length, sepal width, petal length, and petal width (cm).
- Output: the model's predicted class; class probabilities are shown when supported by the saved estimator.
- The saved pickle/joblib artifact must be compatible with the installed scikit-learn and Python versions. If loading fails, reproduce the training environment and re-export the model.
- This is an educational portfolio demo, not a production model or a substitute for botanical assessment.

## Stack

Python · NumPy · scikit-learn · Joblib · Streamlit
