import requests


class WeatherDataFetcher:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, latitude, longitude):
        """
        Λαμβάνει τα τρέχοντα δεδομένα καιρού καθώς και την 24ωρη πρόγνωση.
        """
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
            "hourly": ["temperature_2m"],
            "forecast_days": 1
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            if "current" in data:
                current_data = data["current"]

                # Επεξεργασία ωρών για το γράφημα (κρατάμε μόνο την ώρα HH:MM)
                raw_times = data.get("hourly", {}).get("time", [])[:8]  # Πρώτες 8 ώρες
                formatted_times = [t.split("T")[1][:5] for t in raw_times]
                temperatures = data.get("hourly", {}).get("temperature_2m", [])[:8]

                return {
                    "temperature": current_data.get("temperature_2m"),
                    "humidity": current_data.get("relative_humidity_2m"),
                    "wind_speed": current_data.get("wind_speed_10m"),
                    "times": formatted_times,
                    "forecast_temps": temperatures
                }
            else:
                return None

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Weather API failure: {e}")
            return None




