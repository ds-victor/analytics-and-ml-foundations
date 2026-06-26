import joblib
import numpy as np
import pandas as pd
import os

def predict_price(area, bedrooms, bathrooms, age, location_score, has_garage, has_pool):
    # Use absolute paths
    base_dir = os.path.dirname(__file__)
    model_path = os.path.normpath(os.path.join(base_dir, '../models/house_price_model.pkl'))
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}. Run train.py first.")
        
    model = joblib.load(model_path)
    
    feature_names = ['area_sqft', 'bedrooms', 'bathrooms', 'age_years', 'location_score', 'has_garage', 'has_pool']
    features = np.array([[area, bedrooms, bathrooms, age, location_score, has_garage, has_pool]])
    
    # Convert to DataFrame to avoid feature name warning
    features_df = pd.DataFrame(features, columns=feature_names)
    
    return model.predict(features_df)[0]

if __name__ == '__main__':
    try:
        price = predict_price(1500, 3, 2, 10, 8.5, 1, 0)
        print(f'Predicted price: ${price:,.2f}')
    except Exception as e:
        print(f"Error: {e}")
