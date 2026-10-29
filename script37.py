import requests
from typing import Dict, Any, Optional, Tuple

class GeocodingService:
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
    # Oρίζουμε την συνάρτηση κατασκευαστή με ανώτατο χρονικό όριο = 10
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
    #παίρνει το όνομα της πόλης σε μορφή string και επιστρέφει ένα ζέυγος (lat,lon)
    # πραγματικών αριθμών
    def get_coordinates(self, city_name: str) -> Optional[Tuple[float, float]]:
        params = {
            "name": city_name,
            "count": 1,
            "language": "el",
            "format": "json"
        }

        #Στέλνουμε αίτημα
        #Ελέγχουμε την εγκυρότητα του
        # Μας δίνονται ακατέργαστα δεδομένα σε μορφή json
        # Mας επιστρέφεται μια λίστα με τα αποτελέσματα
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            results = data.get("results")
            if not results:
                print(f"[WARN] Η πόλη '{city_name}' δεν βρέθηκε.")
                return None

            first_match = results[0]
            lat = first_match.get("latitude")
            lon = first_match.get("longitude")
            return (lat, lon)
        # αν για κάποιο λόγο η σύνδεση είναι αδύναμη το σύστημα δεν κρασάρει, επιστρέφει None
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Αποτυχία σύνδεσης στο Geocoding API: {e}")
            return None

if __name__ == "__main__":
    geocoder = GeocodingService()
    coords = geocoder.get_coordinates("Athens")
    print(f"Συντεταγμένες Αθήνας: {coords}")
    





