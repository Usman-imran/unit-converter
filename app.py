import sys
sys.path.append('/your/python/site-packages/path')
import streamlit as st

st.title ("Unit Converter 💫")

# unit conversion

conversion_types = ["Temperature", "Length", "Weight"]

# let user choose converion 

conversion_choice = st.selectbox("Choose Conversion Type", conversion_types)

# Length Conversion
if conversion_choice == "Length":
    length_unit = ["Meters", "Kilometers", "Feet", "Inches","Centimeters"]
    input_value = st.number_input("Enter Length Value:", min_value=0.0, format = "%.2f")
    from_unit = st.selectbox ("From Unit:", length_unit)
    to_unit = st.selectbox ("To Unit:", length_unit)

# conversion Dictionaries
    length_conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.348,
        "Inches": 0.0254,
        "Centimeters": 0.01,
    }

# Conversion Login 
    if st.button("Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success (f'{input_value} {from_unit} is equal to {result} {to_unit}')

# Weight Converion
elif conversion_choice == "Weight":
    weight_unit = ["Gram", "Kilogram", "Pounds", "Ounces"]
    input_value = st.number_input("Enter Weight Value:", min_value=0.0, format = "%.2f")
    from_unit = st.selectbox ("From Unit:", weight_unit)
    to_unit = st.selectbox ("To Unit:", weight_unit)

# Conversion Dictionaries
    weight_conversion = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }

# Conversion Logic
    if st.button("Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success (f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')

# Temperature Conversion
elif conversion_choice == "Temperature":
    temperature_unit = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter Temperature Value:", min_value=0.0, format = "%.2f")
    from_unit = st.selectbox ("From Unit:", temperature_unit)
    to_unit = st.selectbox ("To Unit:", temperature_unit)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit": 
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value
    
    if st.button("Convert"):
        result = convert_temperature (input_value, from_unit, to_unit)
        st.success (f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')