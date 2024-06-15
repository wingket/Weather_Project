#creating the weather forecasting app using framework streamlit python
#Author - Aniket Kadam

import requests
import math
import json
import sys
import streamlit as st


def get_info_weather(location):
    api_key = "8c44287806e2d08826d4954f499e4643"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()   # raise an exception for any http error
    except requests.exceptions.HTTPError as err:
        st.error(f"Error: {err} ")
        return
    try:
        data = response.json()
        if data['cod'] != 200:
            st.error(f"Error: {data['message']}")
            #sys.exit(1)
            return
    except json.JSONDecodeError as err:
        st.error(f"Error: Failed to parse response JSON - {err}")
        return

    #Extract weather info.

    weatherr_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    #convert temp from k to c

    temperature = round(temperature - 273.15, 2)

    #print the weather forecast

    #st.write(data)
    st.write(f"Weather in {location}: {weatherr_description}")
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Humidity: {humidity} %")
    st.write(f"Pressure: {pressure} hPa")

st.header("Weather Information of current Location ")
location=st.text_input("Enter City/Location name: ")
if st.button("Get Weather"):
    get_info_weather(location)