import sys
import os
from pathlib import Path
import pandas as pd
import pytest

# Add scripts directory to path
sys.path.append(str(Path(__file__).parent.parent / "scripts"))

from feature_engineering import run_feature_engineering
from business_impact_calculator import calculate_business_impact

def test_feature_engineering_output_shape():
    """Test that feature engineering returns expected transformed data."""
    X_transformed = run_feature_engineering()
    assert X_transformed is not None
    # We expect some columns after One-Hot Encoding
    assert X_transformed.shape[1] > 4 

def test_business_impact_logic():
    """Test that business impact calculation runs without error."""
    # This script mainly prints, but we can verify it doesn't crash
    try:
        calculate_business_impact()
        success = True
    except Exception:
        success = False
    assert success is True

def test_dataset_exists():
    """Verify the core dataset is in the right place."""
    data_path = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
    assert data_path.exists()
    df = pd.read_csv(data_path)
    assert not df.empty
    assert 'price' in df.columns
