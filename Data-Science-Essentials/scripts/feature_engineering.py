import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def run_feature_engineering():
    """
    Topic 5: Feature Engineering Strategy
    Implementing encoding and scaling for the house price dataset.
    """
    print("--- Topic 5: Feature Engineering Strategy ---")
    
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    if not data_path.exists():
        print("Data not found.")
        return

    df = pd.read_csv(data_path)
    
    # Define features
    categorical_features = ['region', 'property_type']
    numerical_features = ['area_sqft', 'age_years', 'bedrooms', 'bathrooms']
    
    print(f"Processing {len(categorical_features)} categorical and {len(numerical_features)} numerical features.")
    
    # Create transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(), categorical_features)
        ]
    )
    
    # Fit and transform
    X = df[numerical_features + categorical_features]
    X_transformed = preprocessor.fit_transform(X)
    
    print("Transformation complete.")
    print(f"Original shape: {X.shape}")
    print(f"Transformed shape: {X_transformed.shape}")
    
    return X_transformed

if __name__ == "__main__":
    run_feature_engineering()
