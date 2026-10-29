import customtkinter as ctk
from geocoding import GeocodingService
from weatherpj import WeatherDataFetcher
from history_manager import HistoryManager
from charts import WeatherChartBuilder
from config import APP_TITLE

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry("600x750")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        # Backend Services
        self.geocoder = GeocodingService()
        self.fetcher = WeatherDataFetcher()
        self.history_mgr = HistoryManager()

        # Title
        self.title_label = ctk.CTkLabel(self, text=APP_TITLE, font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, pady=(15, 5))

        # Search Frame
        self.search_frame = ctk.CTkFrame(self)
        self.search_frame.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        self.search_frame.grid_columnconfigure(0, weight=1)

        self.city_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Εισάγετε όνομα πόλης...")
        self.city_entry.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

        self.search_btn = ctk.CTkButton(self.search_frame, text="Αναζήτηση", command=self.on_search)
        self.search_btn.grid(row=0, column=1, padx=(5, 10), pady=10)

        # Weather Card Frame
        self.weather_frame = ctk.CTkFrame(self)
        self.weather_frame.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        self.weather_frame.grid_columnconfigure(0, weight=1)

        self.result_city_label = ctk.CTkLabel(self.weather_frame, text="Αναζητήστε μια πόλη",
                                              font=("Arial", 16, "bold"))
        self.result_city_label.grid(row=0, column=0, pady=(10, 2))

        self.temp_label = ctk.CTkLabel(self.weather_frame, text="-- °C", font=("Arial", 32, "bold"))
        self.temp_label.grid(row=1, column=0, pady=2)

        self.humidity_label = ctk.CTkLabel(self.weather_frame, text="Υγρασία: --", font=("Arial", 13))
        self.humidity_label.grid(row=2, column=0, pady=1)

        self.wind_label = ctk.CTkLabel(self.weather_frame, text="Άνεμος: --", font=("Arial", 13))
        self.wind_label.grid(row=3, column=0, pady=(1, 10))

        # Chart Frame
        self.chart_frame = ctk.CTkFrame(self)
        self.chart_frame.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")

        # History OptionMenu
        self.history_menu = ctk.CTkOptionMenu(self, values=["Ιστορικό αναζητήσεων"], command=self.on_history_select)
        self.history_menu.grid(row=4, column=0, padx=20, pady=10)
        self.update_history_menu()

    def update_history_menu(self):
        history = self.history_mgr.load_history()
        if history:
            self.history_menu.configure(values=history)
        else:
            self.history_menu.configure(values=["Ιστορικό αναζητήσεων"])

    def on_search(self):
        city = self.city_entry.get().strip()
        if not city:
            return

        coords = self.geocoder.get_coordinates(city)
        if not coords:
            self.result_city_label.configure(text="Η πόλη δεν βρέθηκε!")
            self.temp_label.configure(text="-- °C")
            self.humidity_label.configure(text="Υγρασία: --")
            self.wind_label.configure(text="Άνεμος: --")
            return

        lat, lon, display_name = coords
        weather = self.fetcher.get_current_weather(lat, lon)
        if weather:
            self.result_city_label.configure(text=display_name)
            self.temp_label.configure(text=f"{weather['temperature']} °C")
            self.humidity_label.configure(text=f"Υγρασία: {weather['humidity']}%")
            self.wind_label.configure(text=f"Άνεμος: {weather['wind_speed']} km/h")

            # Δημιουργία Γραφήματος Θερμοκρασίας
            if weather.get("times") and weather.get("forecast_temps"):
                WeatherChartBuilder.create_temperature_chart(
                    self.chart_frame,
                    weather["times"],
                    weather["forecast_temps"]
                )

            self.history_mgr.add_to_history(display_name)
            self.update_history_menu()

    def on_history_select(self, selected_city):
        if selected_city and selected_city != "Ιστορικό αναζητήσεων":
            self.city_entry.delete(0, "end")
            self.city_entry.insert(0, selected_city)
            self.on_search()


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
