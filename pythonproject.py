#-----------------------------------------------------
# Name: Sudhanshu Kumar
# ERP: RU-26-01999
# Email: sudhanshukumarsingh4566@gmail.com
# section: BCA 1A
# PS No.: 51
#Project Title: Digital Dairy/Notes Manager
#-----------------------------------------------------

import json
from datetime import datetime

FILE_NAME = "diary.txt"


# Load notes from file
def load_notes():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save notes to file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


# Validate date
def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d") == date
    except ValueError:
        return False


# 1. Add Note
def add_note():
    date = input("Date (YYYY-MM-DD): ").strip()

    if not valid_date(date):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    text = input("Text: ").strip()

    if not text:
        print("Note text cannot be empty.")
        return

    notes = load_notes()

    notes.append({
        "date": date,
        "text": text
    })

    save_notes(notes)
    print("Note saved.")

    note_no = len(notes)
    print(f"{note_no} | {date} | {text}")


# 2. View All Notes
def view_notes():
    notes = load_notes()

    if not notes:
        print("No notes found. Your diary is empty.")
        return

    print("All Notes:")

    for i, note in enumerate(notes, start=1):
        print(f"{i} | {note['date']} | {note['text']}")


# 3. Search Notes
def search_notes():
    notes = load_notes()

    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = []

    for i, note in enumerate(notes, start=1):
        if keyword in note["text"].lower():
            found.append((i, note))

    if found:
        print(f"Found {len(found)} notes:")

        for i, note in found:
            print(f"{i} | {note['date']} | {note['text']}")

        print(f"Note(s) deleted: 0. Notes left: {len(notes)}")
    else:
        print("No matching notes found.")


# 4. Delete Note
def delete_note():
    notes = load_notes()

    if not notes:
        print("No notes found. Your diary is empty.")
        return

    try:
        number = int(input("Enter note number to delete: ").strip())
    except ValueError:
        print("Invalid note number.")
        return

    if number < 1 or number > len(notes):
        print(f"Note number {number} not found.")
        return

    deleted_note = notes.pop(number - 1)

    save_notes(notes)

    print(f"Note {number} deleted.")
    print(f"Notes left: {len(notes)}")


# Main Menu
def main():
    while True:
        print("\n===== DIGITAL DIARY / NOTES MANAGER =====")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            search_notes()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            print("Thank you for using Digital Diary!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
