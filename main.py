from geocoding import GeocodingService
from weatherpj import WeatherDataFetcher

def get_weather_for_city(city_name:str):
    geocoder = GeocodingService()
    fetcher = WeatherDataFetcher()
    coords = geocoder.get_coordinates(city_name)
    if not coords:
        print("Sorry cant find the coordinates")
        return

    lat,lon = coords
    weather = fetcher.get_weather_by_coordinates(lat,lon)
    print(f"Weather for: {city_name} ")
    print(weather)

    if __name__ == "__main__":
        get_weather_for_city("Aθήνα")


