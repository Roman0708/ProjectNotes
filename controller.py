class Controller(object):

    def __init__(self,model):
        self.model = model

    def create_note(self, note):
        self.model.create_note(note)

    def notes_exist(self):
        notes = self.model.read_json()
        if len(notes) == 0:
            print("Заметок не найдено")
            return(False)
        else:
            return(True)
        
    def show_note(self, note_id):
        note = self.model.read_note(note_id)
        print(note)

    def show_all_notes(self):
        notes = self.model.read_json()
        for note in notes:
            print(note)
