import sqlite3


class EmployeeDatabase:
    def __init__(self, db_name="employees.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                birth_date DATE NOT NULL,
                gender TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_employee(self, employee):
        self.cursor.execute('''
            INSERT INTO employees (full_name, birth_date, gender)
            VALUES (?, ?, ?)
        ''', (employee.full_name, employee.birth_date, employee.gender))
        self.conn.commit()

    def add_employees_bulk(self, employees):
        self.cursor.executemany('''
            INSERT INTO employees (full_name, birth_date, gender)
            VALUES (?, ?, ?)
        ''', employees)
        self.conn.commit()

    def get_all_employees(self):
        self.cursor.execute('''
            SELECT DISTINCT full_name, birth_date, gender FROM employees ORDER BY full_name
        ''')
        return self.cursor.fetchall()

    def filter_by_gender_and_lastname(self, gender, last_name_start):
        query = '''
               SELECT full_name, birth_date, gender
               FROM employees
               WHERE gender = ? AND full_name LIKE ?
               ORDER BY full_name
           '''
        self.cursor.execute(query, (gender, last_name_start + '%'))
        return self.cursor.fetchall()

    def create_indexes(self):
        self.cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_gender_fullname ON employees (gender, full_name)
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()
