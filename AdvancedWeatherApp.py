# ADVANCED WEATHER APP
# ==========================================

# IMPORT LIBRARIES

import os
import zipfile
import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import MinMaxScaler

print("All libraries imported successfully!")


# ==========================================
# DATA COLLECTION
# ==========================================

def download_weather_data():

    # URL ADDRESS - JENA WEATHER DATASET
    url = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip"

    # FILE NAMES
    zip_path = "jena_climate_2009_2016.csv.zip"
    csv_path = "jena_climate_2009_2016.csv"

    # CHECK IF DATASET ALREADY EXISTS
    if not os.path.exists(csv_path):

        print("Downloading weather data...")

        # DOWNLOAD DATA
        response = requests.get(url, timeout=120)

        # CHECK FOR HTTP ERRORS
        response.raise_for_status()

        # SAVE ZIP FILE
        with open(zip_path, "wb") as file:
            file.write(response.content)

        print("Weather data downloaded successfully!")

        # EXTRACT CSV FILE
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extract(csv_path)

        print("Weather data extracted successfully!")

    else:
        print("Weather dataset already exists!")

    # RETURN CSV FILE PATH
    return csv_path


# ==========================================
# EXECUTE FUNCTION
# ==========================================

file_path = download_weather_data()

print("Dataset location:", file_path)


