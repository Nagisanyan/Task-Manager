#!/usr/bin/env python3
import json
import sys
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Aucune tâche pour le moment.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['text']}")


def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Tâche ajoutée : {text}")


def done_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Indice invalide.")
        return
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print(f"Tâche complétée : {tasks[index - 1]['text']}")


def delete_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Indice invalide.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Tâche supprimée : {removed['text']}")


def print_help():
    print("Usage :")
    print("  python todo.py list")
    print("  python todo.py add \"Texte de la tâche\"")
    print("  python todo.py done <numéro>")
    print("  python todo.py delete <numéro>")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "list":
        list_tasks()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Merci de préciser le texte de la tâche.")
            return
        text = " ".join(sys.argv[2:])
        add_task(text)
    elif command == "done":
        if len(sys.argv) < 3:
            print("Merci de préciser le numéro de la tâche.")
            return
        try:
            index = int(sys.argv[2])
        except ValueError:
            print("Le numéro doit être un entier.")
            return
        done_task(index)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Merci de préciser le numéro de la tâche.")
            return
        try:
            index = int(sys.argv[2])
        except ValueError:
            print("Le numéro doit être un entier.")
            return
        delete_task(index)
    else:
        print_help()


if __name__ == "__main__":
    main()
