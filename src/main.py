
import streamlit as st
import pandas as pd

# Title of the app
st.title("Real-Time Flood Risk Map for Kurdistan")

# Display a brief description
st.write("This app shows flood risk areas based on real-time rainfall predictions and historical data.")

# Load dataset (replace with your actual data loading logic)
def load_data():
    # Example: Load a sample dataset
    data = pd.DataFrame({
        "Location": ["City A", "City B", "City C"],
        "Risk Level": ["High", "Medium", "Low"],
        "Rainfall (mm)": [120, 80, 30]
    })
    return data

# Display the dataset
st.header("Sample Data")
data = load_data()
st.write(data)

# Display a simple map (replace with your actual map data)
st.header("Sample Map")
map_data = pd.DataFrame({
    "lat": [36.1911, 36.2000, 36.2100],  # Example latitudes for Kurdistan
    "lon": [44.0092, 44.0100, 44.0200],  # Example longitudes for Kurdistan
    "risk": ["High", "Medium", "Low"]    # Example risk levels
})
st.map(map_data)

# Add a placeholder for future functionality
st.header("Future Features")
st.write("- Real-time flood risk visualization based on rainfall predictions.")
st.write("- Historical flood risk map using past rainfall data.")
st.write("- Interactive features to explore specific areas.")
