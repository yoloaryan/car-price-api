from pathlib import Path
import pandas as pd
import joblib

CAR_PRICE_API_DIR = Path(__file__).resolve().parent
ROOT_DIR = CAR_PRICE_API_DIR.parent

MODEL_PATH = CAR_PRICE_API_DIR / "random_forest_model.pkl" if (CAR_PRICE_API_DIR / "random_forest_model.pkl").exists() else ROOT_DIR / "random_forest_model.pkl"
COLS_PATH = CAR_PRICE_API_DIR / "feature_columns.pkl" if (CAR_PRICE_API_DIR / "feature_columns.pkl").exists() else ROOT_DIR / "feature_columns.pkl"

_model = None
_feature_columns = None


def load_artifacts():
    global _model, _feature_columns
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _feature_columns is None:
        _feature_columns = joblib.load(COLS_PATH)


import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def preprocess(payload: dict) -> pd.DataFrame:
    """
    Converts raw input into the SAME one-hot encoded column structure used in training.
    """
    df = pd.DataFrame([payload])

    categorical_cols = ["Fuel_Type", "Seller_Type", "Transmission", "Owner", "Car_Name"]
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Efficiently align columns with training feature columns
    df_aligned = df_encoded.reindex(columns=_feature_columns, fill_value=0)

    return df_aligned


def predict_price(payload: dict) -> float:
    load_artifacts()
    X = preprocess(payload)
    pred = _model.predict(X)[0]
    return float(pred)
