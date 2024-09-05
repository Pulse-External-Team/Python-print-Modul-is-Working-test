import os

# Datei zum Speichern der To-Do-Liste
TODO_FILE = "todo_list.txt"

# Lade die vorhandene To-Do-Liste aus der Datei
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [task.strip() for task in file.readlines()]
        return tasks
    return []

# Speichere die To-Do-Liste in die Datei
def save_todo_list(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Zeige die To-Do-Liste an
def show_todo_list(tasks):
    print("\n--- To-Do List ---")
    if not tasks:
        print("Keine Aufgaben vorhanden.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("-------------------\n")

# Füge eine Aufgabe zur To-Do-Liste hinzu
def add_task(tasks):
    task = input("Neue Aufgabe: ").strip()
    if task:
        tasks.append(task)
        save_todo_list(tasks)
        print(f"Aufgabe '{task}' hinzugefügt.\n")
    else:
        print("Leere Aufgaben können nicht hinzugefügt werden.\n")

# Markiere eine Aufgabe als erledigt
def mark_task_done(tasks):
    show_todo_list(tasks)
    try:
        task_number = int(input("Nummer der erledigten Aufgabe: "))
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            save_todo_list(tasks)
            print(f"Aufgabe '{completed_task}' wurde als erledigt markiert.\n")
        else:
            print("Ungültige Nummer.\n")
    except ValueError:
        print("Bitte eine gültige Nummer eingeben.\n")

# Hauptprogramm
def main():
    tasks = load_todo_list()

    while True:
        print("Was möchtest du tun?")
        print("1. To-Do-Liste anzeigen")
        print("2. Aufgabe hinzufügen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Beenden")

        choice = input("Wähle eine Option (1-4): ").strip()

        if choice == "1":
            show_todo_list(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle eine Option von 1 bis 4.\n")

if __name__ == "__main__":
    main()
