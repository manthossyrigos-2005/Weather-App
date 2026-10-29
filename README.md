# 🌤️ Weather Forecast Application

Μια desktop εφαρμογή πρόγνωσης καιρού σε Python, κατασκευασμένη με σύγχρονο **Dark Mode GUI** και υποστήριξη δυναμικών διαγραμμάτων.

---

## 🚀 Χαρακτηριστικά (Features)

* 🔍 **Αναζήτηση Πόλης**: Γεωεντοπισμός σε πραγματικό χρόνο μέσω **Nominatim (OpenStreetMap API)**.
* 🌡️ **Δεδομένα Καιρού**: Λήψη θερμοκρασίας, υγρασίας και ταχύτητας ανέμου μέσω **Open-Meteo API**.
* 📊 **Διαγράμματα Πρόγνωσης**: Δυναμική σχεδίαση γραφήματος θερμοκρασίας με **Matplotlib**.
* 📜 **Ιστορικό Αναζητήσεων**: Αυτόματη αποθήκευση και φόρτωση πρόσφατων αναζητήσεων σε αρχείο **JSON**.
* 🎨 **Σύγχρονο UI**: Περιβάλλον εργασίας βασισμένο στο **CustomTkinter**.

---

## 🛠️ Τεχνολογίες & Βιβλιοθήκες (Tech Stack)

* **Γλώσσα**: Python 3.16
* **GUI**: `customtkinter`
* **APIs & HTTP Requests**: `requests`
* **Charts**: `matplotlib`
* **Data Persistence**: `json`

---

## 📦 Εγκατάσταση & Εκτέλεση (Setup & Usage)
```bash
   git clone [https://github.com/manthossyrigos-2005/Weather-App.git](https://github.com/manthossyrigos-2005/Weather-App.git)
   cd Weather-App
pip install -r requirements.txt
python gui.py(εντολή στο terminal για εκτέλεση του προγράμματος)
Weather-App/
├── gui.py               # Κύριο παράθυρο εφαρμογής & UI
├── weatherpj.py         # Υπηρεσία λήψης δεδομένων καιρού (Open-Meteo)
├── geocoding.py         # Μετατροπή πόλης σε συντεταγμένες (Nominatim)
├── history_manager.py   # Διαχείριση ιστορικού αναζητήσεων (JSON)
├── charts.py            # Δημιουργία διαγραμμάτων (Matplotlib)
├── config.py            # Ρυθμίσεις εφαρμογής
└── requirements.txt     # Απαραίτητες βιβλιοθήκες Python
   
   ```bash
   git clone [https://github.com/manthossyrigos-2005/Weather-App.git](https://github.com/manthossyrigos-2005/Weather-App.git)
   cd Weather-App
