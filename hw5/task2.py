import os

def split_file_path(file_path):
    # Разделить путь на каталог и имя файла
    directory, filename = os.path.split(file_path)
    
    # Разделить имя файла и расширение
    name, extension = os.path.splitext(filename)
    
    return directory, name, extension

# Пример использования:
file_path = "C:/Users/Hp/OneDrive/Рабочий стол/hw8/text.txt"
path, name, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)