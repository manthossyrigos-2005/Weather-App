from geocoding import GeocodingService
from weatherpj import WeatherDataFetcher
from history_manager import HistoryManager
from config import APP_TITLE, MIN_CITY_NAME_LENGTH

# Αρχικοποίηση του manager ιστορικού
history_mgr = HistoryManager()


def get_weather_for_city(city_name: str) -> None:
    geocoder = GeocodingService()
    fetcher = WeatherDataFetcher()

    coords = geocoder.get_coordinates(city_name)
    if not coords:
        print(f"Δεν ήταν δυνατή η εύρεση συντεταγμένων για την πόλη: {city_name}")
        return

    lat, lon = coords
    weather = fetcher.get_weather_by_coordinates(lat, lon)

    if weather:
        # Αποθήκευση της πόλης στο ιστορικό
        history_mgr.save_city(city_name)

        code = weather.get("weather_code")
        desc = (
            fetcher.get_weather_description(code)
            if hasattr(fetcher, "get_weather_description") and code is not None
            else "Δεν διατίθεται"
        )

        print("\n" + "=" * 40)
        print(f" 🌡️  ΚΑΙΡΟΣ ΓΙΑ: {city_name.strip().upper()}")
        print("=" * 40)
        print(f"• Συνθήκες   : {desc}")
        print(f"• Θερμοκρασία: {weather.get('current_temperature')}°C")
        print(f"• Υγρασία    : {weather.get('humidity')}%")
        print(f"• Άνεμος     : {weather.get('wind_speed')} km/h")

        # Εμφάνιση ωριαίας πρόγνωσης (πρώτες 3 ώρες)
        hourly = weather.get("hourly_forecast", {})
        times = hourly.get("time", [])[:3]
        temps = hourly.get("temperature_2m", [])[:3]

        if times and temps:
            print("\n 🕒 Πρόγνωση Επόμενων Ωρών:")
            for t, temp in zip(times, temps):
                hour = t.split("T")[-1]
                print(f"   - {hour} : {temp}°C")

        print("=" * 40 + "\n")


if __name__ == "__main__":
    print(APP_TITLE)
    print("💡 Πληκτρολογήστε 'history' για να δείτε τις τελευταίες αναζητήσεις.")

    while True:
        city = input("\nΔώστε όνομα πόλης (ή 'exit' για έξοδο): ").strip()

        if city.lower() in ["exit", "quit"]:
            print("Ευχαριστούμε που χρησιμοποιήσατε την εφαρμογή! Αντίο 👋")
            break

        if city.lower() == "history":
            history_mgr.display_history()
            continue

        if city.isdigit():
            print("[WARN] Παρακαλώ εισάγετε όνομα πόλης και όχι αριθμούς!")
            continue

        if len(city) < MIN_CITY_NAME_LENGTH:
            print(
                f"[WARN] Το όνομα της πόλης πρέπει να έχει τουλάχιστον {MIN_CITY_NAME_LENGTH} χαρακτήρες."
            )
            continue

        if city:
            get_weather_for_city(city)

