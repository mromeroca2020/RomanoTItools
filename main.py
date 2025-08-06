import tkinter as tk
from tkinter import ttk
from modules import network_diagnostics

class RomanoTItoolsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RomanoTItools - IT Network Suite")
        self.root.geometry("600x400")

        title = ttk.Label(root, text="RomanoTItools", font=("Helvetica", 20))
        title.pack(pady=20)

        ttk.Button(root, text="Network Diagnostics", command=network_diagnostics.run).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RomanoTItoolsApp(root)
    root.mainloop()