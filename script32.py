import tkinter as tk
from tkinter import messagebox
import requests

# Create application window
window = tk.Tk()
window.title("Weather Station")
window.geometry("420x530")
window.configure(bg="#11243B")
window.resizable(False, False)


# Weather descriptions
weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Fog",
    51: "Light drizzle",
    53: "Drizzle",
    55: "Dense drizzle",
    61: "Light rain",
    63: "Rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Rain showers",
    82: "Heavy showers",
    95: "Thunderstorm"
}


def get_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a city!"
        )
        return

    try:
        # Find city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_response = requests.get(
            geo_url,
            params={
                "name": city,
                "count": 1,
                "language": "en"
            },
            timeout=10
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            messagebox.showerror(
                "Error",
                "City not found!"
            )
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "timezone": "auto"
            },
            timeout=10
        )
        response.raise_for_status()

        data = response.json()["current"]

        temperature = data["temperature_2m"]
        humidity = data["relative_humidity_2m"]
        wind = data["wind_speed_10m"]
        code = data["weather_code"]

        condition = weather_codes.get(
            code, "Other conditions"
        )

        # Update graphical interface
        city_label.config(
            text=location["name"]
        )

        temperature_label.config(
            text=f"{temperature}°C"
        )

        condition_label.config(
            text=condition
        )

        humidity_label.config(
            text=f"Humidity: {humidity}%"
        )

        wind_label.config(
            text=f"Wind: {wind} km/h"
        )

    except (requests.RequestException, ValueError, KeyError):
        messagebox.showerror(
            "Error",
            "Could not retrieve weather data."
        )


# Application title
title = tk.Label(
    window,
    text="WEATHER STATION",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#11243B"
)
title.pack(pady=25)


# City input
city_entry = tk.Entry(
    window,
    font=("Arial", 16),
    justify="center",
    bg="#233B56",
    fg="white",
    insertbackground="white"
)
city_entry.pack(pady=10, ipady=8)

city_entry.insert(0, "Athens")


# Search button
search_button = tk.Button(
    window,
    text="GET WEATHER",
    font=("Arial", 13, "bold"),
    bg="#2563EB",
    fg="white",
    command=get_weather
)
search_button.pack(pady=15)


# Weather information
city_label = tk.Label(
    window,
    text="Enter a city",
    font=("Arial", 18),
    fg="white",
    bg="#11243B"
)
city_label.pack(pady=10)

temperature_label = tk.Label(
    window,
    text="--°C",
    font=("Arial", 48, "bold"),
    fg="#FACC15",
    bg="#11243B"
)
temperature_label.pack(pady=10)

condition_label = tk.Label(
    window,
    text="Weather conditions",
    font=("Arial", 16),
    fg="#D4E2F2",
    bg="#11243B"
)
condition_label.pack(pady=5)

humidity_label = tk.Label(
    window,
    text="Humidity: --",
    font=("Arial", 15),
    fg="white",
    bg="#11243B"
)
humidity_label.pack(pady=10)

wind_label = tk.Label(
    window,
    text="Wind: --",
    font=("Arial", 15),
    fg="white",
    bg="#11243B"
)
wind_label.pack(pady=10)


# Press Enter to search
city_entry.bind(
    "<Return>",
    lambda event: get_weather()
)

window.mainloop()










