import datetime
import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='user1',
            passwd='1111',
            database='users'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


curtime = datetime.datetime.now()


def sayHi(users):
    print(f'Рады Вас видеть, {users[0][1]} {users[0][2]}! Хорошего дня!')
    with open('log_work.txt', 'a') as f:
        f.write(f'\n{curtime} || {users[0][1]} {users[0][2]} выполнил вход!')
        f.close()


def remove(users):
    print(f"До свидания, мистер {users[0][1]} {users[0][2]}")
    with open('log_work.txt', 'a') as f:
        f.write(f'\n{curtime} || {users[0][1]} {users[0][2]} покинул нас!')
        f.close()


def run():
    connection = create_connection()
    access = input('Введите 1 - если вход, 2 - если выход\n')
    id = input('Введите Ваш id: ')
    password = input('Введите Ваш пароль: ')
    select_users = f"SELECT * from users WHERE id = {id} and pass = {password}"
    users = execute_read_query(connection, select_users)
    return users, access


while True:
    users, access = run()
    if users == []:
        print('Ошибка при вводе, повторите попытку!')
        users, access = run()
    else:
        pass
    if access == '1':
        sayHi(users)
        users = None
    elif access == '2':
        remove(users)
        users = None
    else:
        print('Выберите вариант 1 либо 2!')

