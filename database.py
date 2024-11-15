import sqlite3


def add_to_database():
    dbmain = sqlite3.connect("main_database.db")
    add_user_table = dbmain.cursor()
    add_user_table.execute('''
                    CREATE TABLE IF NOT EXISTS user_data(
                        id INTEGER PRIMARY KEY,
                        uuid TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        phone TEXT,
                        age TEXT,
                        nrc  TEXT,
                        dob TEXT,
                        auth TEXT)''')

    dbmain.commit()



    


def create_user(user_data):

    dbload = sqlite3.connect("main_database.db")
    cursor = dbload.cursor()
    cursor.execute(''' INSERT INTO user_data(uuid, first_name,last_name, phone, age, nrc, dob,  auth) VALUES(?,?,?,?,?,?,?,?)''', user_data)

    dbload.commit()
    dbload.close()

def read_user_data():

    dbload = sqlite3.connect("main_database.db")
    cursor = dbload.cursor()
    cursor.execute("SELECT uuid, first_name,last_name, phone, age, nrc, dob,  auth FROM user_data")

    user_data = cursor.fetchall()

    dbload.commit()
    dbload.close()

    return user_data
    


def update_user_data():
    print("update user data")


def delete_user_data():
    print("delete user data")





date_of_birth = {"year": 1996, "month": 2, "day": 6}

user_data = {"first_name": "kamukwamba",
             "last_name": "masupha",
             "age": 34,
             "nrc": "365493/73/1",
             "dob": date_of_birth,
             "auth": "admin"
             }

add_to_database()

