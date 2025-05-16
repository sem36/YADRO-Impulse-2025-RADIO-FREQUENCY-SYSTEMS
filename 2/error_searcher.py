import re
import sys

# Проверка количества аргументов
if len(sys.argv) != 3:
    print("Используйте: python error_searcher.py <filename> <word> ")
    sys.exit(1)

def search_in_file(file_path, word):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if re.search(rf'\b{re.escape(word)}\b', line, re.IGNORECASE):
                    print(line.strip())
    except FileNotFoundError:
        print(f"файл '{file_path}' не найдет")

search_in_file(sys.argv[1], sys.argv[2])
