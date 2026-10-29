import json
import os
from typing import List
from config import HISTORY_FILENAME, MAX_HISTORY_ITEMS


class HistoryManager:
    def __init__(self, filename: str = HISTORY_FILENAME):
        self.filename = filename

    def load_history(self) -> List[str]:
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[WARN] Αποτυχία ανάγνωσης ιστορικού: {e}")
            return []

    def save_city(self, city_name: str) -> None:
        history = self.load_history()
        formatted_city = city_name.strip().title()

        # Αφαίρεση διπλότυπου αν υπάρχει ήδη στη λίστα
        if formatted_city in history:
            history.remove(formatted_city)

        # Προσθήκη στην αρχή της λίστας
        history.insert(0, formatted_city)

        # Διατήρηση μόνο των τελευταίων MAX_HISTORY_ITEMS εγγραφών
        history = history[:MAX_HISTORY_ITEMS]

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(history, file, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"[ERROR] Αποτυχία αποθήκευσης στο ιστορικό: {e}")

    def display_history(self) -> None:
        history = self.load_history()

        if not history:
            print("\n 📜 Το ιστορικό αναζητήσεων είναι άδειο.\n")
            return

        print("\n" + "=" * 40)
        print("  ΙΣΤΟΡΙΚΟ ΑΝΑΖΗΤΗΣΕΩΝ")
        print("=" * 40)
        for idx, city in enumerate(history, 1):
            print(f" {idx}. {city}")
        print("=" * 40 + "\n")
