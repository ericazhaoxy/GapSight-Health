# Pipeline (WIP)

Data build + modeling scripts will live here (dataset -> train -> explain).

# Modeling (XGBoost)

This folder contains the XGBoost modeling scaffold for GapSight Health.

## What this does

- Trains XGBoost regression model for a demand index (e.g., anxiety/depression)
- Uses time-based split to reduce leakage
- Prints MAE/RMSE and saves model artifact to `models/`

## Script

- `train_xgb.py`
