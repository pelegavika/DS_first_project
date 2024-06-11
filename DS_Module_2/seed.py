from sqlite3 import Error
import sqlite3

from datetime import datetime
import faker
from random import randint, choice


def create_status(conn, status):

    sql='''INSERT INTO status (name) VALUES(?)'''
    cur=conn.cursor()
    try:
        cur.execute(sql, status)
        conn.commit()
    except Error as e:
        print (e)
    finally:
        cur.close()
    return cur.lastrowid

def create_users(conn, users):

    sql='''INSERT INTO users (fullname, email) VALUES(?, ?)'''
    cur=conn.cursor()
    try:
        cur.execute(sql, users)
        conn.commit()
    except Error as e:
        print (e)
    finally:
        cur.close()
    return cur.lastrowid

def create_tasks(conn, tasks):

    sql='''INSERT INTO tasks (title, description, status_id, user_id) VALUES(?, ?, ?, ?)'''
    cur=conn.cursor()
    try:
        cur.execute(sql, tasks)
        conn.commit()
    except Error as e:
        print (e)
    finally:
        cur.close()
    return cur.lastrowid

# if __name__=='__main__':
#     with create_connection(database) as conn:

NUMBER_USERS = 10
NUMBER_TASKS = 30


def generate_fake_data(number_users, number_tasks):
    fake_users = []
    fake_tasks = []
   
    fake_data = faker.Faker()

# Створимо набір users
    for _ in range(number_users):
        fake_user = (fake_data.name(), fake_data.ascii_email())
        fake_users.append(fake_user)

# Згенеруємо тепер task
    for _ in range(number_tasks):
        fake_tasks.append(fake_data.paragraph(nb_sentences=1))

    return fake_users, fake_tasks

users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)

with sqlite3.connect("./task2") as conn:

    new_status_id = create_status(conn, ("new",))
    inprogress_status_id = create_status(conn, ("in progress",))
    completed_status_id = create_status(conn, ("completed",))

    fake_task_id = 0
    for user in users:
        user_id = create_users(conn, user)
        fake_task = (tasks[fake_task_id], tasks[fake_task_id], new_status_id, user_id)
        create_tasks(conn, fake_task)
        fake_task_id += 1

        fake_task = (tasks[fake_task_id], tasks[fake_task_id], inprogress_status_id, user_id)
        create_tasks(conn, fake_task)
        fake_task_id += 1

        fake_task = (tasks[fake_task_id], tasks[fake_task_id], completed_status_id, user_id)
        create_tasks(conn, fake_task)
        fake_task_id += 1
    # conn.close()
