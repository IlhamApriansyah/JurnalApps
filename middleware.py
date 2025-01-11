import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from controllers import (
    add_journal_entry,
    edit_journal_entry,
    delete_journal_entry,
    get_all_journal_entries,
)

class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Jurnal Pribadi")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Frame untuk tombol
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Tombol untuk menambah, mengedit, menghapus, dan menampilkan entri
        btn_add = tk.Button(button_frame, text="Tambah Entri Jurnal", command=self.add_entry, width=20, bg="#4CAF50", fg="white")
        btn_add.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_edit = tk.Button(button_frame, text="Edit Entri Jurnal", command=self.edit_entry, width=20, bg="#2196F3", fg="white")
        btn_edit.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        btn_delete = tk.Button(button_frame, text="Hapus Entri Jurnal", command=self.delete_entry, width=20, bg="#f44336", fg="white")
        btn_delete.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        btn_show = tk.Button(button_frame, text="Tampilkan Semua Entri Jurnal", command=self.show_entries, width=20, bg="#FFC107", fg="black")
        btn_show.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Textbox untuk konten jurnal
        self.content_text = tk.Text(self.root, height=10, width=40)
        self.content_text.pack(pady=10)

        # Dropdown untuk memilih mood
        self.mood_var = tk.StringVar(value="Baik")
        mood_label = tk.Label(self.root, text="Pilih Mood:", bg="#f0f0f0")
        mood_label.pack()
        mood_options = ["Baik", "Tidak Baik"]
        self.mood_menu = tk.OptionMenu(self.root, self.mood_var, *mood_options)
        self.mood_menu.pack(pady=5)

    def add_entry(self):
        content = self.content_text.get("1.0", tk.END).strip()
        mood = self.mood_var.get()
        if content:
            add_journal_entry(content, mood)
            messagebox.showinfo("Info", "Entri jurnal berhasil ditambahkan.")
            self.content_text.delete("1.0", tk.END)  # Menghapus konten setelah ditambahkan

    def edit_entry(self):
        entry_id = simpledialog.askstring("Input", "Masukkan ID entri yang ingin diedit:")
        new_content = simpledialog.askstring("Input", "Masukkan konten baru:")
        new_mood = simpledialog.askstring("Input", "Masukkan mood baru (Baik/Tidak Baik):")
        if edit_journal_entry(entry_id, new_content, new_mood):
            messagebox.showinfo("Info", "Entri jurnal berhasil diedit.")
        else:
            messagebox.showerror("Error", "Entri tidak ditemukan.")

    def delete_entry(self):
        entry_id = simpledialog.askstring("Input", "Masukkan ID entri yang ingin dihapus:")
        delete_journal_entry(entry_id)
        messagebox.showinfo("Info", "Entri jurnal berhasil dihapus.")

    def show_entries(self):
        entries_window = tk.Toplevel(self.root)
        entries_window.title("Semua Entri Jurnal")
        entries_window.geometry("400x300")
        entries_window.configure(bg="#f0f0f0")

        entries = get_all_journal_entries()
        if not entries:
            label = tk.Label(entries_window, text="Tidak ada entri jurnal.", bg="#f0f0f0")
            label.pack(pady=10)
            return
        
        for entry in entries:
            entry_text = f"ID: {entry.id} | Tanggal: {entry.date} | Konten: {entry.content} | Mood: {entry.mood}"
            label = tk.Label(entries_window, text=entry_text, bg="#f0f0f0")
            label.pack(pady=5)

            # Menambahkan garis pemisah
            separator = ttk.Separator(entries_window, orient='horizontal')
            separator.pack(fill='x', pady=5)
