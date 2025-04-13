# Description: A simple unit converter app that converts length, weight, time, mass, and temperature units.
    
import streamlit as st

# App Title


st.title("🔄 Unit Converter App 🚀")
st.markdown("### Converts 📏 Length, ⚖️ Weight, ⏰ Time, ⚖️ Mass, and 🌡️ Temperature Instantly")
st.write("Welcome to Aqsa's Unit Converter App! Select a category, enter a value and get the converted result in real-time")

category = st.selectbox("⭐ Choose a Category To Convert", ["Length", "Weight", "Time", "Mass", "Temperature"])

# Conversion Function

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    elif category == "Mass":
        if unit == "Grams to Kilograms":
            return value / 1000
        elif unit == "Kilograms to Grams":
            return value * 1000

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9

    return 0

 # Select Conversion

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
elif category == "Mass":
    unit = st.selectbox("⚖️ Select Conversion", ["Grams to Kilograms", "Kilograms to Grams"])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

value = st.number_input("Enter the value to convert")

# Add custom CSS for button styling
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: orange;
        color: white;
        border-radius: 5px;
        border: 2px solid green;
        padding: 10px 20px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
 
# Result Button

if st.button("Convert"):
    result = convert_units(category, value, unit, )
    st.success(f" Your Converted Result is {result:.2f}!")