import tkinter as tk
from middleware import JournalApp

# Membuat antarmuka pengguna
root = tk.Tk()
app = JournalApp(root)

# Menjalankan aplikasi
root.mainloop()