import gui
import db
import views.get_tasks as gt

import datetime

while True:
    command = gui.ask()

    if command == "exit":
        break

    command = command.split()
    cmd_by_usr = command[0]

    if cmd_by_usr == "add":
        task_name = " ".join(command[1:])
        str_date = str(datetime.datetime.now().date())
        db.insert_task(task_name, str_date)
    elif cmd_by_usr == "tasks":
        gt.view_all_tasks()
