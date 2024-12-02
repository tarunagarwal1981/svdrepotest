import streamlit as st
from svd.svd_model import SVDModel
from svd.svd_validator import SVDValidator
from svd.svd_exporter import SVDExporter

# Streamlit app
st.title("Standardised Vessel Dataset (SVD) Viewer & Validator")

# Form for user input
st.sidebar.header("Noon Report Input")
vessel_name = st.sidebar.text_input("Vessel Name")
speed = st.sidebar.number_input("Speed (knots)", min_value=0.0)
fuel_consumption = st.sidebar.number_input("Fuel Consumption (MT)", min_value=0.0)
weather_conditions = st.sidebar.selectbox("Weather Condition", ["Good", "Moderate", "Poor"])

# Submit Button
if st.sidebar.button("Validate"):
    # Create the SVD model
    svd_data = SVDModel(
        vessel_name=vessel_name,
        speed=speed,
        fuel_consumption=fuel_consumption,
        weather_conditions=weather_conditions,
    )
    
    # Validate the data
    is_valid, errors = SVDValidator.validate(svd_data)
    
    if is_valid:
        st.success("Validation Passed!")
        # Export options
        st.download_button("Download as JSON", SVDExporter.export_to_json(svd_data), "noon_report.json", "application/json")
        st.download_button("Download as CSV", SVDExporter.export_to_csv(svd_data), "noon_report.csv", "text/csv")
    else:
        st.error("Validation Failed")
        st.json(errors)

# Display Sample Data
if st.checkbox("Show Sample SVD Dataset"):
    sample_data = SVDModel.get_sample()
    st.json(sample_data)
