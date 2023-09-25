
def is_leap_year(year):
    """
    Проверяет, является ли год високосным.
    
    Год является високосным, если он кратен 4, но не кратен 100,
    за исключением случаев, когда он кратен 400.
    
    :param year: Год для проверки
    :type year: int
    :return: True, если год високосный, в противном случае False
    :rtype: bool
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def is_valid_date(date_str):
    """
    Проверяет, является ли дата корректной в формате DD.MM.YYYY.
    
    :param date_str: Дата в формате DD.MM.YYYY
    :type date_str: str
    :return: True, если дата корректная, в противном случае False
    :rtype: bool
    """
    try:
        day, month, year = map(int, date_str.split('.'))
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if month == 2:
            if is_leap_year(year):
                return 1 <= day <= 29
            else:
                return 1 <= day <= 28
        elif month in [4, 6, 9, 11]:
            return 1 <= day <= 30
        else:
            return 1 <= day <= 31
    except ValueError:
        return False

# Пример использования:
if __name__ == "__main__":
    date = "31.12.2022"
    if is_valid_date(date):
        print(f"{date} - Эта дата существует.")
    else:
        print(f"{date} - Эта дата не существует.")