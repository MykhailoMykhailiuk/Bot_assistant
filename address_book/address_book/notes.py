from collections import UserDict, defaultdict


class Tag:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, tag):
        if type(tag) != Tag:
            return False
        
        return self.name == tag.name

    def __str__(self):
        return f'{self.name}'


class Tags(UserDict):
    
    def add_tag(self, name):
        new_tag = Tag(name)
        if new_tag in self.data.values():
            return f'Tag with name {name} already exists!'
        
        index = len(self.data) + 1 if len(self.data) > 0 else 1
        self.data[index] = new_tag
        return f'Tag with name {name} succesfully created!'
    
    def get_tags(self):
        tags = '{:<30}\n'.format('Tag')
        for tag_name in self.data.values():
            tags += '{:<30}\n'.format(tag_name)
        return tags
    
    def get_tag_name(self, tag_index):
        return self.data[tag_index].name


class Item:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return f"{self.title} {self.text}"
    
    def __eq__(self, item):
        if type(item) != Item:
            return False
        
        return self.title == item.title # and self.text == item.text


class Notes(UserDict):

    def __init__(self):
        super().__init__()
        self.tags = Tags()
        self.notes_tags = defaultdict(list)

    def add_note(self, title, text):
        new_note = Item(title, text)
        if new_note in self.data.values():
            return f"Note with title {title} already exists!"
        
        idx = len(self.data)+1 if len(self.data) > 0 else 1
        self.data[idx] = new_note
        return f"Note with title {title} was succesfully added!" # self.get_notes()
    
    def get_notes(self, notes_id_list=None):
        notes = '|{:^30}|{:^50}|{:^30}|\n'.format("Title", "Text", "Tags")
        if notes_id_list == None or len(notes_id_list) == 0:
            for key, value in self.data.items():
                notes += '|{:^30}|{:<50}|{:^30}|\n'.format(value.title, value.text, self.get_note_tags(key))
        else:
            for key, value in self.data.items():
                if key in notes_id_list:
                    notes += '|{:^30}|{:<50}|{:^30}|\n'.format(value.title, value.text, self.get_note_tags(key))
        return notes

    def find_notes(self, text_to_find):
        text_to_find = text_to_find.lower()
        notes_found = Notes()
        for note in self.data.values():
            if note.title.lower().find(text_to_find) != -1\
                or note.text.lower().find(text_to_find) != -1:
                notes_found.add_note(note.title, note.text)
        
        return notes_found
    
    def find_notes_by_tag(self, tag_name=None, tag_id=None):
        if tag_id == None and tag_name == None:
            return str()
        
        notes_found = list()
        for node_id, tag_ids in self.notes_tags.items():
            if tag_id in tag_ids:
                notes_found.append(node_id)

        return self.get_notes(notes_id_list=notes_found)

    def delete_note(self, title_text):
        for id, note in self.data.items():
            if title_text.lower().strip() in note.title.lower():
                del self.data[id]
                return "Removed note"
        return "No note with such title"
    
    def edit_note(self, title_text, new_text):
        for id, note in self.data.items():
            if title_text.lower().strip() in note.title.lower() or title_text.lower().strip() in note.title.lower():
                self.data[id] = Item(note.title, new_text)
                return self.get_notes()
        return "No note with such text"

    def get_note_id(self, note_title):
        note = Item(note_title, None)
        note_index = None
        for key, value in self.data.items():
            if value == note:
                note_index = key
                break
        
        return note_index
    
    def get_tag_id(self, tag_name):
        tag = Tag(tag_name)
        tag_index = None
        for key, value in self.tags.data.items():
            if value == tag:
                tag_index = key
        
        return tag_index

    def add_tag_for_note(self, tag_name, note_title):
        note_index = self.get_note_id(note_title)
        if note_index == None:
            return f"Such note with title '{note_title}' doesn't exist"
        
        tag_index = self.get_tag_id(tag_name)
        if tag_index == None:
            return f"Such tag '{tag_name}' doesn't exist"
        
        if tag_index in self.notes_tags[note_index]:
            return f"Tag '{tag_name}' was already linked to the note '{note_title}'."
        else:
            self.notes_tags[note_index].append(tag_index)
            return f"Tag '{tag_name}' for the note '{note_title}' was created succesfully."

    def get_note_tags(self, note_id):
        tags = list()
        if note_id != None and note_id >= 0:
            for tag in self.notes_tags[note_id]:
                tags.append(self.tags.get_tag_name(tag))
        
        return ', '.join(tags)