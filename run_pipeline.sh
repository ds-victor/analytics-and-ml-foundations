#!/bin/bash
echo "Running ML Series Pipeline..."

# 1. Prepare BI Data
python 01_Business_Analytics/scripts/prepare_bi_data.py && echo "✓ Data prepared"

# 2. Train Model
python 03_ML_Foundations/src/train.py && echo "✓ Model trained"

# 3. Predict Example
python 03_ML_Foundations/src/predict.py && echo "✓ Prediction complete"

# 4. Generate EDA Report
python 02_Data_Analytics/scripts/eda_report.py && echo "✓ EDA complete"

echo "Pipeline finished. Check repository folders for outputs."
