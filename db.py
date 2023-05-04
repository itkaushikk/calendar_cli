import sqlite3

def insert_task(task_name):
    con = sqlite3.connect("db.db")
    cur = con.cursor()

    res = cur.execute("SELECT TKID FROM TLST ORDER BY TKID DESC")
    last_task_id = res.fetchone()
    if last_task_id:
        task_id = last_task_id[0] + 1
    else:
        task_id = 1

    insert_query = """INSERT INTO TLST (TKID, TKNM, TKST) VALUES ({}, {}, 'Active')""".format(task_id, task_name)

    cur.execute(insert_query)
    con.commit()
    con.close()

def get_tasks():
    con = sqlite3.connect("db.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM TLST")
    all_tasks = res.fetchall()

    return all_tasks