# print("===== DIGITAL DIARY =====")
# print("1. Add Note")
# print("2. View All Notes")
# print("3. Search Notes")
# print("4. Delete Note")
# print("5. Exit")

# choice = input("Apni choice enter karo: ")

# if choice == "1":
#     print("Add Note selected")
# elif choice == "2":
#     print("View Notes selected")
# elif choice == "3":
#     print("Search Notes selected")
# elif choice == "4":
#     print("Delete Note selected")
# elif choice == "5":
#     print("Exiting Digital Diary")
# else:
#     print("Invalid choice! Dobara try karo.")

from datetime import datetime

FILE_NAME = "diary.txt"


def load_notes():
    notes = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.rstrip("\n").split("|", 2)

                if len(parts) == 3:
                    try:
                        number = int(parts[0])
                        date = parts[1]
                        text = parts[2]
                        notes.append({
                            "number": number,
                            "date": date,
                            "text": text
                        })
                    except ValueError:
                        continue

    except FileNotFoundError:
        pass

    return notes


def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for note in notes:
            line = (
                str(note["number"]) + "|"
                + note["date"] + "|"
                + note["text"] + "\n"
            )
            file.write(line)


def add_note():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    text = input("Enter note text: ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    if text == "":
        print("Note text cannot be empty.")
        return

    notes = load_notes()

    if notes:
        number = max(note["number"] for note in notes) + 1
    else:
        number = 1

    note = {
        "number": number,
        "date": date,
        "text": text
    }

    notes.append(note)
    save_notes(notes)
    print("Note saved.")


def view_notes():
    notes = load_notes()

    if not notes:
        print("No notes found. Your diary is empty.")
        return

    print("\nYour Diary:")
    for note in notes:
        print(
            note["number"], "|",
            note["date"], "|",
            note["text"]
        )


def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()

    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    notes = load_notes()
    found = []

    for note in notes:
        if note["text"].lower().find(keyword) != -1:
            found.append(note)

    if not found:
        print("No matching notes found.")
        return

    print("Found", len(found), "note(s):")

    for note in found:
        print(
            note["number"], "|",
            note["date"], "|",
            note["text"]
        )


def delete_note():
    try:
        number = int(input("Enter note number to delete: ").strip())
    except ValueError:
        print("Please enter a valid note number.")
        return

    notes = load_notes()

    for note in notes:
        if note["number"] == number:
            notes.remove(note)
            save_notes(notes)
            print("Note", number, "deleted.")
            return

    print("Note number", number, "not found.")


def main():
    while True:
        print("\n===== DIGITAL DIARY =====")
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
            print("Exiting Digital Diary.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()