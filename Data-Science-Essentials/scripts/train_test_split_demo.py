import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

def demonstrate_splits():
    """
    Topic 10: Train-Test Split Deep Dive
    Comparing Random and Stratified splits.
    """
    print("--- Topic 10: Train-Test Split Demo ---")
    
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    if not data_path.exists(): return
    df = pd.read_csv(data_path)
    
    # 1. Random Split
    train_r, test_r = train_test_split(df, test_size=0.2, random_state=42)
    
    # 2. Stratified Split (on region)
    train_s, test_s = train_test_split(df, test_size=0.2, random_state=42, stratify=df['region'])
    
    print("Original Region Distribution:")
    print(df['region'].value_counts(normalize=True))
    
    print("\nRandom Split Region Distribution (Test Set):")
    print(test_r['region'].value_counts(normalize=True))
    
    print("\nStratified Split Region Distribution (Test Set):")
    print(test_s['region'].value_counts(normalize=True))
    
    print("\nInsight: Stratified split ensures your test set is representative of the whole population.")

if __name__ == "__main__":
    demonstrate_splits()
