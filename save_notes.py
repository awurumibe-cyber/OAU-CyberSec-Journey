from datetime import datetime

note = input("What did you learn today? ")
timestamp = datetime.now()

with open("cc_notes.txt", "a") as file:
    file.write(f"{timestamp} - {note}\n")
