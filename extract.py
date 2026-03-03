import requests
import pandas as pd
import os  # We need this to check if the file already exists

# -----------------------------
# EXTRACT
# -----------------------------
latitude = 33.3152
longitude = 44.3661

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current_weather=true"
    f"&timezone=auto"
)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # -----------------------------
    # TRANSFORM
    # -----------------------------
    current_weather = data.get("current_weather", {})
    df = pd.DataFrame([current_weather])
    
    # Add metadata so we know where this data came from
    df["latitude"] = latitude
    df["longitude"] = longitude
    df["timezone"] = data.get("timezone")

    # -----------------------------
    # LOAD (The Upgrade)
    # -----------------------------
    file_name = "baghdad_weather.csv"

    # Check if the file already exists
    if os.path.isfile(file_name):
        # If it exists, append to it (mode='a') and DO NOT write headers
        df.to_csv(file_name, mode='a', header=False, index=False)
        print(f"✅ Data appended to {file_name}")
    else:
        # If it does not exist, create it (mode='w') and write headers
        df.to_csv(file_name, mode='w', header=True, index=False)
        print(f"🆕 Created new file: {file_name}")
        
    print(df)

else:
    print(f"❌ Error: {response.status_code}")
