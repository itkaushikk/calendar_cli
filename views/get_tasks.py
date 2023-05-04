from db import get_tasks 

def view_all_tasks():
    all_tasks = get_tasks()

    print("Task ID   | Task Description")
    print("-"*10 + " " + "-"*50)
    for val in all_tasks:
        if val[2] == "Active":
            id = val[0]
            str_id = str(id)
            length_str_id = len(str_id)
            before_zeros = "0"*(5-length_str_id)
            display_id = before_zeros + str_id

            task = val[1]

            display_task = display_id + (" "*5) + "|" + " " + task

            print(display_task)
