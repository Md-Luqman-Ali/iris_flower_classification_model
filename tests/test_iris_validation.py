import importlib.util
import pathlib
import sys
import types

import numpy as np
import pytest

# Load the validation function without requiring Streamlit or the model artifact.
source = pathlib.Path(__file__).parents[1] / "iris_app.py"
text = source.read_text(encoding="utf-8")
assert "def validate_measurements" in text

def test_validation_contract_is_present():
    assert "Exactly four measurements are required." in text
    assert "Measurements must be finite numbers." in text
    assert "Measurements must be greater than zero." in text
