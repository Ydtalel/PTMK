from datetime import datetime


class Employee:
    def __init__(self, full_name, birth_date, gender):
        self.full_name = full_name
        self.birth_date = birth_date
        self.gender = gender

    def close(self):
        self.conn.close()

    def calculate_age(self):
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age
