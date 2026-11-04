# Digital Diary / Notes Manager

A simple Python 3 console application for creating and managing diary notes. Notes are stored locally in a text file, so they remain available the next time the program runs.

## Features

- Add a note with a date and text.
- View all saved notes.
- Search notes by keyword (search is case-insensitive).
- Delete a note by its number.
- Validate note dates using the `YYYY-MM-DD` format.
- Keep notes in a local text file, with each note's date and text.

## Requirements

- Python 3
- No third-party packages are required for the described functionality.

## Run the program

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the Python file:

   ```bash
   python pythonproject.py
   ```

   On some systems, use `python3 main.py` instead. If your Python file has a different name, replace `main.py` with that filename.

## How to use

Use the menu shown in the console:

1. **Add** a note. Enter a date such as `2026-10-10` and non-empty note text.
2. **View all** notes saved in the diary.
3. **Search** notes by a keyword.
4. **Delete** a note by its displayed number.

The app reports when the diary is empty, when a search finds no matches, and when a requested note number does not exist. Dates must use `YYYY-MM-DD`.

## Data storage

Notes are saved in a local text file. Keep that file with the program if you want to retain your notes when moving the project. The file is created or updated by the application.

## Project information

- **Project:** Digital Diary / Notes Manager
- **Language:** Python 3
- **Concepts:** strings, files, searching, and functions
- **Academic project:** BCA, Rungta International Skills University, School of Information Technology
