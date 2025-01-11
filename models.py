from datetime import datetime

# Variabel global untuk menyimpan ID terakhir
last_id = -1

class Jurnal:
    def __init__(self, content, mood=None):
        global last_id
        last_id = (last_id + 1) % 100000  # Menghasilkan ID berurutan dari 0-99999
        self.id = last_id
        self.date = datetime.now().strftime("%Y-%m-%d")  # Tanggal saat ini
        self.content = content
        self.mood = mood