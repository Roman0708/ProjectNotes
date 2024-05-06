import json

from noteclass import Note

class ModelJSON(object):

    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

    def read_json(self):
        notes_list = list()
        try:

            with open(self.filename,'r',encoding='utf-8') as note:
                notes_json = note.read()
                #print(f'notes_json - {notes_json}')
                note.close()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            #print(f'data - {data}')
            for item in data:
                #print(f'item - {item}')
                notes_list.append(Note(item['id'],item['date'],item['title'],item['text']))
            return(notes_list)
    
        except ValueError as e:
            print(f'ValueError - {self.notes}{e}')
            return self.notes
        except TypeError:
            print(f'TypeError - {self.notes}')
            return self.notes
    
    def write_json(self,notes):
        json_strings_list = list()
        for note in notes:
            json_strings_list.append({'id':note.note_id,'date':note.date,'title':note.title,'text':note.text})
        
        notes_json = json.dumps(json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.filename,'w',encoding='utf-8') as note:
            note.write(notes_json)
            note.close()

    def create_note(self,note):
        #print(note)
        self.notes = self.read_json()
        max_id = 0
        for item in self.notes:
            if item.note_id > max_id:
                max_id = item.note_id
        note_id = max_id + 1
        note.note_id = int(note_id)
        #print(note_id)
        self.notes.append(note)
        self.write_json(self.notes)

    def read_note(self, search_id):
        self.notes = self.read_json()
        for note in self.notes:
            if note.note_id == search_id:
                return(note)
        else:
            print("\nЗаметки с таким id не найдено\n")
            return(False)
        
    def update_note(self,id_to_update,note):
        self.notes = self.read_json()
        for item in self.notes:
            if item.note_id == id_to_update:
                item.date = note.date
                item.title = note.title
                item.text = note.text
        self.write_json(self.notes)

    def delete_note(self, id_to_delete):
        self.notes = self.read_json()
        for index, note in enumerate(self.notes):
            if note.note_id == id_to_delete:
                del self.notes[index]

        self.write_json(self.notes)