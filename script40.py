import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WeatherChartBuilder:
    @staticmethod
    def create_temperature_chart(parent_frame, times, temperatures):
        """
        Δημιουργεί ένα διάγραμμα θερμοκρασίας και το ενσωματώνει στο Tkinter frame.
        """
        # Καθαρισμός προηγούμενων γραφημάτων στο frame
        for widget in parent_frame.winfo_children():
            widget.destroy()

        # Δημιουργία Figure & Axes του Matplotlib
        fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
        fig.patch.set_facecolor('#2b2b2b')  # Dark background για να ταιριάζει με CustomTkinter
        ax.set_facecolor('#2b2b2b')

        # Σχεδίαση γραμμής θερμοκρασίας
        ax.plot(times, temperatures, marker='o', color='#1f538d', linewidth=2, markersize=5)

        # Ρυθμίσεις αξόνων & κειμένου
        ax.tick_params(colors='white', labelsize=8)
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_title("Πρόγνωση Θερμοκρασίας", color='white', fontsize=10, pad=10)
        ax.set_ylabel("°C", color='white', fontsize=9)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Ενσωμάτωση του Matplotlib Figure στο CustomTkinter Frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)