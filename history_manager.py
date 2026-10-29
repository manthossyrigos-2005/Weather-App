import json
import os


class HistoryManager:
    def __init__(self, filename="search_history.json"):
        self.filename = filename

    def load_history(self):
        """Φορτώνει το ιστορικό αναζητήσεων από το αρχείο JSON."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Αποτυχία ανάγνωσης ιστορικού: {e}")
            return []

    def add_to_history(self, city_name):
        """Προσθέτει μια νέα πόλη στο ιστορικό (αποφεύγοντας διπλότυπα)."""
        history = self.load_history()

        # Αφαίρεση αν υπάρχει ήδη για να μπει στην αρχή
        if city_name in history:
            history.remove(city_name)

        history.insert(0, city_name)  # Προσθήκη στην αρχή της λίστας
        history = history[:10]  # Κρατάμε μόνο τις 10 τελευταίες αναζητήσεις

        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[ERROR] Αποτυχία αποθήκευσης ιστορικού: {e}")
