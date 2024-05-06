from noteclass import Note
from modelJSON import ModelJSON
from controller import Controller
import datetime

def start():
    c = Controller(ModelJSON("notes.json"))

    while True:
        command = input('1 - создать заметку\n'
                        '2 - прочитать заметку\n'
                        '3 - показать все заметки\n'
                        '4 - обновить заметку\n'
                        '5 - удалить заметку\n'
                        '9 - выход\n'
                        'Введите команду: ')

        if command == '9':
            break

        elif command == '1':
            c.create_note(get_note_data())

        elif command == '2':
            if c.notes_exist():
                c.show_note(get_note_id())

        elif command == '3':
            if c.notes_exist():
                c.show_all_notes()

        elif command == '4':
            if c.notes_exist():
                id_to_update = get_note_id()
                if c.model.read_note(id_to_update):
                    c.model.update_note(id_to_update,get_note_data())
                
        elif command == '5':
            if c.notes_exist():
                id_to_delete = get_note_id()
                if c.model.read_note(id_to_delete):
                    c.model.delete_note(id_to_delete)

def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    return Note(note_id, date, title, text)

def get_note_id():
    while True:
        get_number = input('Введите id заметки: ')
        if get_number.isdigit() and int(get_number) > 0:
            return(int(get_number))
        else:
            print('Введите целое положительное число')