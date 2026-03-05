import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Data
# We tell Python: "Read the CSV, and treat the 'time' column as actual clock time, not just text."
df = pd.read_csv("baghdad_weather.csv")
df['time'] = pd.to_datetime(df['time'])

# 2. Setup the "Canvas"
plt.figure(figsize=(10, 6))  # Make it 10 inches wide, 6 inches tall

# 3. Draw the Line
plt.plot(df['time'], df['temperature'], marker='o', linestyle='-', color='b')

# 4. Add Labels (The "Why")
plt.title("Baghdad Hourly Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True) # Add a grid so it looks professional

# 5. Save the Painting
plt.savefig("weather_graph.png")
print("✅ Graph saved as 'weather_graph.png'")