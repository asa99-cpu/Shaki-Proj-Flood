import pandas as pd

def load_historical_data():
    # Example: Load historical rainfall data (replace with your actual data)
    historical_data = pd.DataFrame({
        "Year": [2020, 2021, 2022],
        "Rainfall (mm)": [150, 200, 180],
        "Flood Risk": ["High", "Medium", "High"]
    })
    return historical_data

def load_realtime_data():
    # Example: Load real-time rainfall predictions (replace with your actual data)
    realtime_data = pd.DataFrame({
        "Location": ["City A", "City B", "City C"],
        "Predicted Rainfall (mm)": [120, 80, 30],
        "Risk Level": ["High", "Medium", "Low"]
    })
    return realtime_data
