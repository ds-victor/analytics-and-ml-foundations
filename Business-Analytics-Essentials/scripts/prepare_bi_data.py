import pandas as pd
import os

def prepare_data():
    # Use absolute paths
    base_dir = os.path.dirname(__file__)
    data_path = os.path.normpath(os.path.join(base_dir, '../data/raw/real_estate_dataset.csv'))
    output_path = os.path.normpath(os.path.join(base_dir, '../data/processed/bi_data.csv'))
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.read_csv(data_path)
    agg = df.groupby(['property_type', 'year_sold']).agg(
        avg_price=('price', 'mean'),
        total_sales=('id', 'count')
    ).reset_index()
    
    agg.to_csv(output_path, index=False)
    print(f'BI data saved to {output_path}')

if __name__ == '__main__':
    prepare_data()
