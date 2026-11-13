# Iris Flower Classification

An interactive machine-learning demo that predicts an Iris species from four flower measurements. This project demonstrates a complete beginner-friendly classification workflow packaged as a Streamlit application.

<p align="center">
  <a href="https://github.com/Md-Luqman-Ali/iris_flower_classification_model"><img src="https://img.shields.io/badge/Project-Machine%20Learning-6C63FF?style=for-the-badge" alt="Machine learning project"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

## Project overview

The app accepts sepal length, sepal width, petal length and petal width (centimetres), then returns the species predicted by the saved estimator. The model artifact is stored in the repository as `iris_model.pkl`.

## Demo status

**Live demo:** Not published yet. A public URL will be added after deployment and a successful smoke test.  
**Application entry point:** `iris_app.py`

## Features

- Interactive Streamlit interface for entering flower measurements.
- Input validation for finite, positive measurement values.
- Cached model loading for app sessions.
- Predicted class display and probabilities when supported by the estimator.
- Reproducible local setup instructions.

## Technology

Python · NumPy · scikit-learn · Joblib · Streamlit

## Repository contents

| File | Purpose |
|---|---|
| `iris_app.py` | Streamlit application |
| `iris_model.pkl` | Saved trained model artifact |
| `requirements.txt` | Python dependencies |

## Run locally

Use Python 3.10 as a starting point, especially if the saved estimator was trained with an older scikit-learn release.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run iris_app.py
```

## Deploy on Streamlit Community Cloud

1. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub.
2. Create an app from this repository and select branch `main`.
3. Set the main file to `iris_app.py`.
4. Select a Python version compatible with the saved model artifact.
5. Deploy and test the app with representative inputs.
6. Add the generated public URL to this README only after confirming it loads and predicts successfully.

Keep `iris_model.pkl` in the repository root. Pickled scikit-learn estimators can be version-sensitive; if model loading fails, recreate the training environment and export a compatible artifact rather than silently changing dependency versions.

## Example inputs

| Example | Sepal length | Sepal width | Petal length | Petal width |
|---|---:|---:|---:|---:|
| Setosa example | 5.1 | 3.5 | 1.4 | 0.2 |
| Versicolor example | 6.0 | 2.9 | 4.5 | 1.5 |
| Virginica example | 6.5 | 3.0 | 5.2 | 2.0 |

These are illustrative inputs, not a guarantee of a particular model output.

## Validation and limitations

- The saved model and the installed Python/scikit-learn versions must be compatible.
- Predictions depend on the training data and fitted estimator.
- This is an educational portfolio project, not a production botanical diagnostic tool.

## Author

**Md Luqman Ali** · [GitHub](https://github.com/Md-Luqman-Ali) · [LinkedIn](https://www.linkedin.com/in/mdluqmanali/)
