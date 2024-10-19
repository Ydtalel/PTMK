import string
import time
from random import choice, randint

from db_manager import EmployeeDatabase
from employee import Employee


def create_employee_table():
    db = EmployeeDatabase()
    db.create_table()
    db.close()
    print("Table 'employees' has been created successfully.")


def add_employee_record(full_name, birth_date, gender):
    db = EmployeeDatabase()
    employee = Employee(full_name, birth_date, gender)
    db.add_employee(employee)
    db.close()
    print(f"Employee {full_name} has been added to the database.")
    print(f"Age of {full_name}: {employee.calculate_age()} years old.")


def show_all_employees():
    db = EmployeeDatabase()
    employees = db.get_all_employees()

    print(f"{'Full Name':<30} {'Birth Date':<12} {'Gender':<8} {'Age'}")
    print("=" * 60)

    for emp_data in employees:
        employee = Employee(*emp_data)
        age = employee.calculate_age()
        print(f"{employee.full_name:<30} {employee.birth_date:<12} {employee.gender:<8} {age}")

    db.close()


def generate_random_name(gender):
    first_names_male = ["Ivan", "Petr", "Alexey", "Sergey", "Nikolay"]
    first_names_female = ["Anna", "Maria", "Elena", "Olga", "Tatiana"]

    last_name = choice(["Ivanov", "Petrov", "Sidorov", "Nikolaev", "Smirnov"])
    patronymic = choice(["Ivanovich", "Petrovich", "Sergeevich", "Nikolaevich"])

    if gender == "Male":
        first_name = choice(first_names_male)
    else:
        first_name = choice(first_names_female)
        last_name = last_name + 'a'
        patronymic = patronymic.replace('ich', 'na')

    return f"{last_name} {first_name} {patronymic}"


def generate_random_birthdate():
    year = randint(1950, 2010)
    month = randint(1, 12)
    day = randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"


def generate_bulk_employees():
    db = EmployeeDatabase()
    employees = []

    for _ in range(999900):
        gender = choice(["Male", "Female"])
        full_name = generate_random_name(gender)
        birth_date = generate_random_birthdate()
        employees.append((full_name, birth_date, gender))

    for _ in range(100):
        full_name = f"F{choice(string.ascii_lowercase)}-{generate_random_name('Male')}"
        birth_date = generate_random_birthdate()
        employees.append((full_name, birth_date, "Male"))

    db.add_employees_bulk(employees)
    db.close()
    print("1,000,000 employees have been generated and inserted into the database.")


def filter_male_with_lastname_F():
    db = EmployeeDatabase()

    start_time_before = time.time()
    results_before = db.filter_by_gender_and_lastname("Male", "F")
    end_time_before = time.time()
    time_before_optimization = end_time_before - start_time_before

    print(f"Query time before optimization: {time_before_optimization:.4f} seconds")

    db.create_indexes()

    start_time_after = time.time()
    results_after = db.filter_by_gender_and_lastname("Male", "F")
    end_time_after = time.time()
    time_after_optimization = end_time_after - start_time_after

    print(f"Query time after optimization: {time_after_optimization:.4f} seconds")

    print(f"{'Full Name':<30} {'Birth Date':<12} {'Gender':<8} {'Age'}")
    print("=" * 60)

    for emp_data in results_after:
        employee = Employee(*emp_data)
        age = employee.calculate_age()
        print(f"{employee.full_name:<30} {employee.birth_date:<12} {employee.gender:<8} {age}")

    db.close()
