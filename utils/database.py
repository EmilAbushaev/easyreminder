import sqlite3


class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY,"
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "telegram_id TEXT);"
                     "CREATE TABLE IF NOT EXISTS persons("
                     "id INTEGER PRIMARY KEY,"
                     "person_name TEXT,"
                     "person_date TEXT);"
                     )
            self.cursor.executescript(query)
            self.connection.commit()

        except sqlite3.Error as Error:
            print('Ошибка при создании', Error)

    def add_user(self, user_name, user_phone, telegram_id):
        self.cursor.execute(
            "INSERT INTO users (user_name, user_phone, telegram_id) VALUES (?,?,?)",
            (user_name, user_phone, telegram_id)
        )
        self.connection.commit()

    def select_user_id(self, telegram_id):
        users = self.cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()

    def add_person(self, person_name, person_date):
        self.cursor.execute(
            "INSERT INTO persons (person_name, person_date) VALUES (?,?)",
            (person_name, person_date)
        )
        self.connection.commit()

    def db_select_all(self, table_name):
        result = self.cursor.execute("SELECT * FROM {}".format(table_name))
        return result.fetchall()

    def delete_person(self, person_name):
        result = self.cursor.execute("DELETE FROM persons WHERE person_name = {}".format(person_name))
        return result.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
