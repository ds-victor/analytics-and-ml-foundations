import pandas as pd
from pathlib import Path

def demonstrate_problem_framing():
    """
    Topic 1: Problem Framing Demo
    Translating business objectives into technical metrics for House Price Prediction.
    """
    print("--- Topic 1: Problem Framing & Scoping ---")
    
    # Define Business Objectives
    objectives = {
        "Goal": "Predict house prices to assist the sales team.",
        "Metric": "Root Mean Squared Error (RMSE)",
        "Threshold": "$25,000",
        "Target Variable": "price"
    }
    
    for key, value in objectives.items():
        print(f"{key}: {value}")
        
    # Simulate loading data and defining the target
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    
    if data_path.exists():
        df = pd.read_csv(data_path)
        print(f"\nDataset loaded successfully from: {data_path}")
        print(f"Target Variable '{objectives['Target Variable']}' is present: {objectives['Target Variable'] in df.columns}")
        print(f"Number of observations: {len(df)}")
    else:
        print(f"\nWarning: Dataset not found at {data_path}")

if __name__ == "__main__":
    demonstrate_problem_framing()
