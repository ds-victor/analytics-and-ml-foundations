import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

def compare_baseline_models():
    """
    Topic 6: Model Selection & Trade-offs
    Comparing Linear Regression and Random Forest.
    """
    print("--- Topic 6: Model Selection Baseline ---")
    
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    if not data_path.exists(): return
    
    df = pd.read_csv(data_path)
    
    # Simple feature selection (numeric only for baseline)
    X = df[['area_sqft', 'age_years', 'bedrooms', 'bathrooms']]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        rmse = root_mean_squared_error(y_test, preds)
        print(f"\n{name}:")
        print(f"  MAE:  ${mae:,.2f}")
        print(f"  RMSE: ${rmse:,.2f}")

if __name__ == "__main__":
    compare_baseline_models()
