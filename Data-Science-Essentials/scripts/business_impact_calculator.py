import pandas as pd

def calculate_business_impact():
    """
    Topic 8: Business Translation
    Quantifying the ROI of improved model accuracy.
    """
    print("--- Topic 8: Business Impact Calculator ---")
    
    # Assumptions
    avg_property_value = 450000
    transactions_per_year = 1000
    manual_error_rate = 0.08  # 8% error in pricing
    model_error_rate = 0.04   # 4% error in pricing
    
    manual_total_error = avg_property_value * manual_error_rate * transactions_per_year
    model_total_error = avg_property_value * model_error_rate * transactions_per_year
    
    savings = manual_total_error - model_total_error
    
    print(f"Average Property Value: ${avg_property_value:,}")
    print(f"Annual Transactions: {transactions_per_year}")
    print(f"Manual Pricing Error (Total): ${manual_total_error:,.2f}")
    print(f"Model Pricing Error (Total):  ${model_total_error:,.2f}")
    print(f"\nPotential Annual Savings/Gain: ${savings:,.2f}")
    print("------------------------------------------")
    print("Insight: Reducing pricing error by half can save the company millions in lost commission or over-pricing inventory.")

if __name__ == "__main__":
    calculate_business_impact()
