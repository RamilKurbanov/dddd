
import argparse

def is_leap_year(year):
 

    def is_valid_date(date_str):


    def main():
        parser = argparse.ArgumentParser(description="Проверка корректности даты в формате DD.MM.YYYY.")
        parser.add_argument("date", type=str, help="Дата для проверки в формате DD.MM.YYYY")
        args = parser.parse_args()
    
        if is_valid_date(args.date):
            print(f"{args.date} - Эта дата существует.")
        else:
            print(f"{args.date} - Эта дата не существует.")

    if __name__ == "__main__":
      main()