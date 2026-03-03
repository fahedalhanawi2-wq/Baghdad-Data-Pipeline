# Import required libraries
import requests          # For making HTTP API requests
import pandas as pd      # For data manipulation and DataFrame handling

# -----------------------------
# EXTRACT STEP
# -----------------------------

# Define Baghdad's geographic coordinates
latitude = 33.3152
longitude = 44.3661

# Define the Open-Meteo API endpoint URL
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current_weather=true"
)

# Send GET request to fetch weather data
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    raise Exception(f"API request failed with status code {response.status_code}")

# Convert response to JSON (Python dictionary)
data = response.json()

# -----------------------------
# TRANSFORM STEP
# -----------------------------

# Extract only the 'current_weather' section from the JSON response
current_weather = data.get("current_weather", {})

# Convert the dictionary into a pandas DataFrame
# Since current_weather is a single record (dictionary),
# we wrap it inside a list to create a single-row DataFrame
df = pd.DataFrame([current_weather])

# Optional: Add metadata columns (recommended in real ETL pipelines)
df["latitude"] = data.get("latitude")
df["longitude"] = data.get("longitude")
df["timezone"] = data.get("timezone")

# Reorder columns for better structure (optional but cleaner)
df = df[
    [
        "time",
        "temperature",
        "windspeed",
        "winddirection",
        "weathercode",
        "is_day",
        "latitude",
        "longitude",
        "timezone",
    ]
]

# -----------------------------
# LOAD STEP
# -----------------------------

# Save the DataFrame to a CSV file
# index=False prevents pandas from adding an extra index column
df.to_csv("baghdad_weather.csv", index=False)

# Print confirmation and preview
print("Weather data successfully saved to baghdad_weather.csv")
print(df)
