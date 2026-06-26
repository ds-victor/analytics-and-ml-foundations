import pandas as pd
from pathlib import Path

def run_fairness_audit():
    """
    Topic 9: Ethics & Fairness
    Checking for disparate impact across locations.
    """
    print("--- Topic 9: Fairness Audit ---")
    
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    if not data_path.exists(): return
    df = pd.read_csv(data_path)
    
    # Group by region and check average prices
    region_stats = df.groupby('region')['price'].agg(['mean', 'std', 'count']).reset_index()
    
    print("Average House Price by Region:")
    print(region_stats)
    
    # Calculate Disparate Impact Ratio (Simple version)
    max_price = region_stats['mean'].max()
    min_price = region_stats['mean'].min()
    disparate_ratio = min_price / max_price
    
    print(f"\nDisparate Impact Ratio (Min/Max Price): {disparate_ratio:.2f}")
    
    if disparate_ratio < 0.8:
        print("Warning: Potential bias detected. Price differences across regions exceed 20%.")
        print("Action: Investigate if these differences are purely structural or influenced by proxy variables.")
    else:
        print("Fairness check passed: Price distribution is relatively balanced across regions.")

if __name__ == "__main__":
    run_fairness_audit()
