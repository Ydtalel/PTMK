import sys

from utils import (create_employee_table, add_employee_record, show_all_employees, generate_bulk_employees,
                   filter_male_with_lastname_F)


def main():
    if len(sys.argv) < 2:
        print("Error: No mode specified.")
        sys.exit(1)

    mode = sys.argv[1]
    modes = {
        "1": create_employee_table,
        "2": lambda: add_employee_record(sys.argv[2], sys.argv[3], sys.argv[4]),
        "3": show_all_employees,
        "4": generate_bulk_employees,
        "5": filter_male_with_lastname_F,
    }

    if mode in modes:
        try:
            modes[mode]()
        except IndexError:
            print("Error: Not enough arguments for this mode.")
            sys.exit(1)
    else:
        print(f"Mode {mode} is not supported.")


if __name__ == "__main__":
    main()
