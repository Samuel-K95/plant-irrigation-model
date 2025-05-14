import requests

url = "http://localhost:8000/predict"  # Change if hosted elsewhere

payload = {
    "features": {
        "Temperature": 27.0,           
        "Soil_Humidity": 60.0,         
        "Time": 14.0,                  
        "Soil_Moisture": 1000,         
        "rainfall": 0.5,               
        "Air_temperature_C": 26.5,     
        "Wind_speed_Kmh": 5.0,         
        "Air_humidity_": 50.0,         
        "Pressure_KPa": 101.3          
    }
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
