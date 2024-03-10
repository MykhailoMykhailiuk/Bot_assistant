# BOT-Assistatnt
###Your personal assistant
This bot will significantly simplify your usage of your phonebook. It enables note creation and seamless navigation between them. Your personal assistant will sort any folder with your files.

###Features
- **Contact Management**: Add, edit, delete contacts.
- **Notes Management**: Write, edit, delete notes with titles and text.
- **Tagging**: Tag notes for better navigation.
- **Search and Filter**: Search contacts by name, search notes by title or text, and find notes by tags.
- **Folder Sorting**: Sort files in a folder based on file extensions into predefined categories.

###Installation
1. Clone repository:  https://github.com/Vladyslaw/address-book-team-project

2. Navigate to the address_book package directory: cd address_book
3. Install dependencies: pip install -e .

###Usage

####Running the application

To start the application, run the `run.py` script: python run.py

####Commands help

    -'add': Bot saves the new contact, you should input:
                <name>
                <phone> number 10 digits format
                <date of birthday> "DD.MM.YYYY" format; (optional)
                <email> "name@test.com" format; (optional)
                <address> (optional)
                <pass> if you want to skip optionals
    -'birthday': Bot shows the nearest contacts birthday by given term (default: 7 days):
                <depth in days>
    -'close': Bot completes its work
    -'create tag': Bot creates the tag
    -'delete': Bot deletes the contact
                <name>
    -'edit address': Bot edits the address for contact:
                <name>
                <address>
    -'edit birthday': Bot edits the birthday for contact:
                <name>
                <date of birthday>
    -'edit email': Bot edits the email for contact:
                <name>
                <email>
    -'edit note': Bot edits the note:
                <title>
                <text>
    -'edit phone': Bot edits the phone for contact:
                <name>
                <phone>
                <new phone>
    -'exit': Bot completes its work
    -'find notes by tags': Bot searchs the notes by tag:
                <tag>
    -'good bye': Bot completes its work
    -'hello': Greet the bot
    -'help': Bot shows the help info
    -'link tag': Bot attaches a tag to the note:
                <title>
                <tag>'
    -'phone': Bot displays the phone number for the given name:
                <name>
    -'remove note': Bot removes the note by title:
                <title>
    -'show all': Bot displays all saved contacts
    -'show notes': Bit displays all saved notes
    -'search notes': Bot searchs the notes by title:
                <title>
    -'search phone': Bot displays the contact at your request
    -'sort folder': Bot sort the folder by file's type (image, documents, music, video, archive, other):
                <path to folder>
    -'write note': Bot saves the note:
                <title>
                <text> (optional)
###File Structure
- **address_book/**
  - **bot.py**: Contains the main logic for the address book bot.
  - **classes.py**: Defines the classes for contacts and notes management.
  - **folder_sorter.py**: Implements functionality for sorting files in a folder.
  - **notes.py**: Handles operations related to notes, including tagging.
  - **run.py**: Entry point for running the address book application.
  - **\_\_init__.py**: Initializes the address book package.

###Acknowledgements
Acknowledgements for individuals that helped inspire, create and improve product.
* Vladyslav Kuzmych - team leader
* Yelyzaveta Melikhova - developer
* Oleksiy Storozhuk - developer
* Yurii Tymoshenko - developer
* Mykhailo Mykhailiuk - developer
