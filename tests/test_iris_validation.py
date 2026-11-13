from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_iris_app_contains_measurement_validation():
    source = (ROOT / "iris_app.py").read_text(encoding="utf-8")
    assert "def validate_measurements(values):" in source
    assert "Exactly four measurements are required." in source
    assert "Measurements must be finite numbers." in source
    assert "Measurements must be greater than zero." in source
