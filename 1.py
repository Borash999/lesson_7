# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
from datetime import datetime

def check_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        print("Дата {} введена корректно.".format(date_str))
    except ValueError:
        print("Дата {} введена некорректно.".format(date_str))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверка корректности даты")
    parser.add_argument("date", help="Дата в формате YYYY-MM-DD для проверки")
    args = parser.parse_args()
    check_date(args.date)
