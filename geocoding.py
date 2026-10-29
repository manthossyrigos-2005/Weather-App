import requests


class GeocodingService:
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"

    def get_coordinates(self, city_name):
        """
        Μετατρέπει το όνομα μιας πόλης σε συντεταγμένες (lat, lon)
        και επιστρέφει το επίσημο όνομα προβολής.
        """
        params = {
            "q": city_name,
            "format": "json",
            "limit": 1
        }
        # Το User-Agent είναι υποχρεωτικό από την πολιτική χρήσης του OpenStreetMap API
        headers = {
            "User-Agent": "WeatherApp/1.0 (Python Weather Desktop Application)"
        }

        try:
            response = requests.get(self.base_url, params=params, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data:
                lat = float(data[0]["lat"])
                lon = float(data[0]["lon"])
                # Κρατάμε μόνο το κύριο όνομα της πόλης/περιοχής
                display_name = data[0]["display_name"].split(",")[0]
                return lat, lon, display_name
            else:
                print(f"[WARN] Η πόλη '{city_name}' δεν βρέθηκε.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Geocoding API failure: {e}")
            return None