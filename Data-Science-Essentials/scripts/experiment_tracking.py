import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from pathlib import Path

def train_with_tracking():
    """
    Topic 7: Experiment Tracking
    Logging a Random Forest run with MLflow.
    """
    print("--- Topic 7: Experiment Tracking with MLflow ---")
    
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    if not data_path.exists(): return
    df = pd.read_csv(data_path)
    
    X = df[['area_sqft', 'age_years', 'bedrooms', 'bathrooms']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # MLflow tracking
    mlflow.set_experiment("House_Price_Prediction")
    
    with mlflow.start_run():
        n_estimators = 100
        max_depth = 5
        
        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        
        preds = model.predict(X_test)
        rmse = root_mean_squared_error(y_test, preds)
        
        # Log params and metrics
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("rmse", rmse)
        
        # Log model
        mlflow.sklearn.log_model(model, "random_forest_model")
        
        print(f"Model trained with RMSE: ${rmse:,.2f}")
        print("Experiment tracked in MLflow (check ./mlruns)")

if __name__ == "__main__":
    train_with_tracking()
