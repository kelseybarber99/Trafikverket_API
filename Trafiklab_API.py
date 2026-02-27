import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
# -----------------------------
# CONFIG
# -----------------------------
API_URL = "https://api.trafikinfo.trafikverket.se/v2/data.json"
API_KEY = "b8b27bc2bfb64dc8a6eadc942f70035b"  # Replace with your actual key
STATION_ID = "222"        # Tullinge

payload_stations = {
    "REQUEST": {
        "LOGIN": {"authenticationkey": API_KEY},
        "QUERY": {
            "objecttype": "WeatherMeasurepoint", "namespace": "road.weatherinfo",
            "includefields": ["MeasurementStationId", "Name", "County"]
        }
    }
}

response = requests.post(API_URL, json=payload_stations)
stations = response.json().get("RESPONSE", {}).get("RESULT", [])[0].get("WeatherMeasurepoint", [])
print(stations)
for s in stations:
    if "Tullinge" in s.get("Name", ""):
        print(s)


# # -----------------------------
# # Calculate date 7 days ago
# # -----------------------------
# seven_days_ago = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S")

# # -----------------------------
# # JSON payload for the API request
# # -----------------------------
# payload = {
#     "REQUEST": {
#         "LOGIN": {"authenticationkey": API_KEY},
#         "QUERY": {
#             "objecttype": "WeatherObservation",
#             "filter": [
#                 {"field": "MeasurementStationId", "operator": "equals", "value": STATION_ID},
#                 {"field": "ObservationTime", "operator": "greaterthanorequal", "value": seven_days_ago}
#             ],
#             "includefields": [
#                 "MeasurementStationId",
#                 "ObservationTime",
#                 "AirTemperature",
#                 "RoadTemperature",
#                 "Precipitation",
#                 "WindSpeed",
#                 "WindDirection"
#             ]
#         }
#     }
# }

# # -----------------------------
# # Make the POST request
# # -----------------------------
# response = requests.post(API_URL, json=payload)
# data = response.json()

# # -----------------------------
# # Parse observations
# # -----------------------------
# observations = data.get("RESPONSE", {}).get("RESULT", [])[0].get("WeatherObservation", [])
# if not observations:
#     print("No data found for the last 7 days.")
# else:
#     # Convert to DataFrame
#     df = pd.DataFrame(observations)
#     # Convert ObservationTime to datetime
#     df['ObservationTime'] = pd.to_datetime(df['ObservationTime'])
#     # Sort by time ascending
#     df = df.sort_values('ObservationTime')
#     print(df)

#     # Optional: save to CSV
#     df.to_csv("tullinge_weather_last7days.csv", index=False)
#     print("\nSaved data to tullinge_weather_last7days.csv")