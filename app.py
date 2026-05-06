import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import numpy as np
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Recta(tk.Tk):
    titulo = "Función lineal"

    def __init__(self):
        super().__init__()
        self.title("Funciones lineales f(x) = mx + b")
        self.geometry("900x600")
        self.minsize(820, 540)

        self.configure(bg="#f5f5f5")

        self.construir_recta()
        self.construir_grafica()
        self.graficar()

    def construir_recta(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        left_panel = tk.Frame(self, bg="#eaf3ff", bd=1, relief="solid")
        left_panel.grid(row=0, column=0, padx=16, pady=16, sticky="ns")

        right_panel = tk.Frame(self, bg="#fffaf2", bd=1, relief="solid")
        right_panel.grid(row=0, column=1, padx=(0, 16), pady=16, sticky="nsew")
        right_panel.rowconfigure(0, weight=1)
        right_panel.columnconfigure(0, weight=1)

        tk.Label(left_panel, text="Recta lineal", bg="#eaf3ff", fg="#1f4e79", font=("Arial", 18, "bold")).grid(
            row=0, column=0, padx=16, pady=(16, 8), sticky="w"
        )
        tk.Label(
            left_panel,
            text="Escribe la pendiente m y el valor b.",
            bg="#eaf3ff",
            justify="left",
            wraplength=220,
        ).grid(row=1, column=0, padx=16, pady=(0, 14), sticky="w")

        tk.Label(left_panel, text="m:", bg="#eaf3ff", fg="#204060").grid(row=2, column=0, padx=16, pady=(4, 2), sticky="w")
        self.entry_m = tk.Entry(left_panel, width=18)
        self.entry_m.grid(row=3, column=0, padx=16, pady=(0, 10), sticky="w")
        self.entry_m.insert(0, "1")

        tk.Label(left_panel, text="b:", bg="#eaf3ff", fg="#204060").grid(row=4, column=0, padx=16, pady=(4, 2), sticky="w")
        self.entry_b = tk.Entry(left_panel, width=18)
        self.entry_b.grid(row=5, column=0, padx=16, pady=(0, 14), sticky="w")
        self.entry_b.insert(0, "0")

        tk.Button(left_panel, text="Graficar", command=self.graficar, width=16, bg="#4f8cff", fg="white", activebackground="#3572d6", activeforeground="white", relief="flat").grid(
            row=6, column=0, padx=16, pady=(0, 8), sticky="w"
        )
        tk.Button(left_panel, text="Limpiar", command=self.limpiar, width=16, bg="#ffb36b", fg="white", activebackground="#e59447", activeforeground="white", relief="flat").grid(
            row=7, column=0, padx=16, pady=(0, 14), sticky="w"
        )

        self.result_label = tk.Label(left_panel, text="f(x) = x", bg="#eaf3ff", fg="#1f4e79", font=("Arial", 12, "bold"))
        self.result_label.grid(row=8, column=0, padx=16, pady=(0, 16), sticky="w")

        tk.Label(
            left_panel,
            text="Si los datos no son números, la gráfica no cambia.",
            bg="#eaf3ff",
            justify="left",
            wraplength=220,
            fg="#4d4d4d",
        ).grid(row=9, column=0, padx=16, pady=(0, 16), sticky="w")

        self.plot_container = right_panel

    def construir_grafica(self):
        self.figure = Figure(figsize=(7, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor("#fff7ec")
        self.ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.6)
        self.ax.set_title(self.titulo)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.axhline(0, color="black", linewidth=0.8)
        self.ax.axvline(0, color="black", linewidth=0.8)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_container)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def _get_values(self):
        try:
            m = float(self.entry_m.get().strip())
            b = float(self.entry_b.get().strip())
        except ValueError:
            raise ValueError("Los valores de m y b deben ser números válidos.")
        return m, b

    def graficar(self):
        try:
            m, b = self._get_values()
        except ValueError as error:
            messagebox.showerror("Datos incorrectos", str(error))
            return

        x = np.linspace(-10, 10, 200)
        y = m * x + b

        self.ax.clear()
        self.ax.set_facecolor("#fff7ec")
        self.ax.plot(x, y, color="#d62728", linewidth=2, label=f"f(x) = {m:g}x + {b:g}")
        self.ax.axhline(0, color="black", linewidth=0.8)
        self.ax.axvline(0, color="black", linewidth=0.8)
        self.ax.set_title(self.titulo)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.6)
        self.ax.set_xlim(-10, 10)
        self.ax.legend(loc="best")

        self.result_label.configure(text=f"f(x) = {m:g}x + {b:g}")
        self.canvas.draw()

    def limpiar(self):
        self.entry_m.delete(0, tk.END)
        self.entry_b.delete(0, tk.END)
        self.entry_m.insert(0, "1")
        self.entry_b.insert(0, "0")
        self.result_label.configure(text="f(x) = x")
        self.ax.clear()
        self.ax.set_facecolor("#fff7ec")
        self.ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.6)
        self.ax.set_title(self.titulo)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.axhline(0, color="black", linewidth=0.8)
        self.ax.axvline(0, color="black", linewidth=0.8)
        self.canvas.draw()


if __name__ == "__main__":
    app = Recta()
    app.mainloop()
