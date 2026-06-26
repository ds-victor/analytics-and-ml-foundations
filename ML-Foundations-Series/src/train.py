import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train():
    # Use absolute paths
    base_dir = os.path.dirname(__file__)
    data_path = os.path.normpath(os.path.join(base_dir, '../data/raw/real_estate_dataset.csv'))
    model_path = os.path.normpath(os.path.join(base_dir, '../models/house_price_model.pkl'))

    df = pd.read_csv(data_path)
    
    # Validation
    if len(df) == 0:
        raise ValueError("Dataset is empty. Provide at least 10 samples for training.")
    if len(df) < 10:
        raise ValueError(f"Insufficient samples ({len(df)}). Need minimum 10 for train-test split.")

    features = ['area_sqft', 'bedrooms', 'bathrooms', 'age_years', 'location_score', 'has_garage', 'has_pool']
    X = df[features]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    joblib.dump(model, model_path)
    print('Model saved.')

if __name__ == '__main__':
    train()
