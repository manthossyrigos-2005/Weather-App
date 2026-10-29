# WEATHER APP
# εισάγουμε την βιβλιοθήκη requests με την οποία θα μπορούμε να στέλνουμε αιτήματα σε
# weather APIs και θα λαμβάνουμε τα καιρικά δεδομένα σε μορφή json
import requests
# εισάγουμε συγκεκριμένα εργαλεία απο τη βιβλιοθήκη τα οποία θέλουμε να χρησιμοποιήσουμε
# Dict: λίστα με ζευγάρια πχ humidity : 60%
# Any : ενδέχεται να περίεχονται αριθμοί,λέξεις κλπ
# Opt : μια τιμή μπορεί να επιστρέψει τα ζητούμενα δεδομένα ή και None(σημαντικό για την ασφάλεια της εφαρμογής)
from typing import Dict, Any, Optional
# Δημιουργία Κλάσης "Συλλέκτης Δεδομένων Καιρού"
class WeatherDataFetcher:
    # Εισαγωγή του συνδέσμου απο τον οποίο θα συλλέγουμε τα δεδομένα
    # Στην κορυφή της κλάσης για να μπορούμε να παρέμβουμε γρήγορα
    # Σε περίπτωση αλλαγής διεύθυνσης
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    # Ορίζουμε συνάρτηση κατασκευαστή με ανώτατο όριο αναμονης
    def __init__(self, timeout: int = 10):
        # Αποθηκεύω σε μία μεταβλητή το ανώτατο όριο χρόνου
        self.timeout = timeout

        # Oρίζουμε νέα συνάρτηση για την αναλυτική περιγραφή του καιρού
        # latitude , longtitude σε μορφή float
        # Επιστρέφει ή None ή τα πραγματικά δεδομένα καιρού σε μορφή κειμένου/τιμών κλπ
        def get_weather_by_coordinates(self, lat: float, lon: float) -> Optional[Dict[str, Any]]:
            # Δημιουργία λεξικού με όνομα parameters
            # Tωρινά - ωριαία δεδομένα
            # Ρύθμιση του timezone με την ώρα της εκάστοτε περιοχής
            parameters = {
                "latitude":lat,
                "longitude":lon,
                "current":["temperature_2m","relative_humidity_2m","weather_code","wind_speed_10m"],
                "hourly ":["temperature_2m","percipitation_probability"],
                "timezone": "auto"
            }
            # Δημιουργία διχτυού ασφαλείας
            # Mε την requests δημιουργούμε ένα αίτημα για την διεύθυνση(URL),τις παραμέτρους και το time limit
            # Mετατροπή δεδομένων από μορφή JSON σε Dict
            # Απομόνωση - Καθαρισμός των καιρικών δεδομένων(raw data) με την parse_weather_data
            # Σε περίπτωση αργής σύνδεσης η python αποθηκεύει το σφάλμα στην μεταβλητή e:
            try:
                response = requests.get(self.BASE_URL, parameters = parameters, timeout = self.timeout)
                response.raise_for_status()
                raw_data = response.json()
                return self._parse_weather_data(raw_data)
            except requests.exceptions.RequestException as e:
                print("Aποτυχία Σύνδεσης στο Weather API")
                return None
            




