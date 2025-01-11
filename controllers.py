from models import Jurnal

jurnal = []

def add_journal_entry(content, mood):
    entry = Jurnal(content, mood)
    jurnal.append(entry)
    return entry.id

def edit_journal_entry(entry_id, new_content, new_mood):
    entry = find_entry_by_id(entry_id)
    if entry:
        entry.content = new_content
        entry.mood = new_mood
        return True
    return False

def delete_journal_entry(entry_id, new_content, new_mood):
    entry = find_entry_by_id(entry_id)
    if entry:
        jurnal.remove(entry)
        return True
    return False

def get_all_journal_entries():
    return jurnal

def find_entry_by_id(entry_id):
    for entry in jurnal:
        if entry.id == entry_id:
            return entry
        return None
    
def get_entries_by_date(date):
    hasil = [entry for entry in jurnal if entry.date == date]
    return hasil

def get_entries_by_mood(mood):
    hasil = [entry for entry in jurnal if entry.mood == mood]
    return hasil