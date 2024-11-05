import pytest

from string_Utils import StringUtils

string_Utils = StringUtils()

def test_capitilize():

# Позитивные тесты

   assert string_Utils.capitilize('skypro') == 'Skypro'                 # С заглавной буквы

   assert string_Utils.capitilize('   skypro'.strip()) == 'Skypro'      # пробелы в начале

   assert string_Utils.capitilize('skypro   '.strip()) == 'Skypro'      # Пробелы в конце

   assert string_Utils.capitilize('') == ''     # пустая строка

   assert string_Utils.capitilize(' ') == ' '     # строка с пробелом 


# Негативные тесты

   assert string_Utils.capitilize('') == ''    # Пустая строка

   assert string_Utils.capitilize(' ') == ' '  # Строка с пробелом

   assert string_Utils.capitilize('0') == '0'  # Строка с нулем

   assert string_Utils.capitilize('😁') == '😁'  # Строка со смайликом


# Тестирование метода trim

def test_trim():

 # Позитивные тесты

   assert string_Utils.trim('   skypro') == 'skypro'  # Пробелы в начале

   assert string_Utils.trim('skypro') == 'skypro'     # Без пробелов

   assert string_Utils.trim('sky pro') == 'sky pro'   # С пробелом в середине

   assert string_Utils.trim('skypro ') == 'skypro '   # C пробелом в конце


# Негативные тесты

   assert string_Utils.trim('  ') == ''                     # Только пробелы

   assert string_Utils.trim('$%^&*"%^') == '$%^&*"%^'       # Только спецсимоволы

   assert string_Utils.trim('') == ''                       # пустая строка

   assert string_Utils.trim('😁😁😁') == '😁😁😁'        # Только эмодзи


# Тестирование метода to_list

def test_to_list():
    
# Позитивные тесты

   assert string_Utils.to_list('a,b,c') == ['a', 'b', 'c']            # Запятая

   assert string_Utils.to_list('1:2:3', ':') == ['1', '2', '3']       # Двоеточие разделитель

   assert string_Utils.to_list('1;2;3', ';') == ['1', '2', '3']       # точка с запятой разделитель

   assert string_Utils.to_list('1/2/3', '/') == ['1', '2', '3']       # Разделитель "/"

   assert string_Utils.to_list('понедельник вторник среда четверг пятница суббота воскресение', ' ') == ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресение'] 
                                                                       # Разделитель пробел

# Негативные тесты

   assert string_Utils.to_list('1😁2😁3', '😁') == ['1', '2', '3']    # Эмодзи разделитель

   assert string_Utils.to_list('1-2-3', '-') == ['1', '2', '3']         # Тире разделитель

   assert string_Utils.to_list('1_2_3', '_') == ['1', '2', '3']         # нижнее подчеркивание

   assert string_Utils.to_list('1%2%3', '%') == ['1', '2', '3']         # спецсимвол разделитель



# Тестирование метода contains

def test_contains():
     
# Позитивные тесты

   assert string_Utils.contains('SkyPro', 'S') is True  # Символ найден

   assert string_Utils.contains('abc', 'abc') is True  # Полное совпадение


# Негативные тесты
   assert string_Utils.contains('SkyPro', 'U') is False               # Символ не найден

   assert string_Utils.contains('', 'a') is False                     # Пустая строка

   assert string_Utils.contains('', '') is True                       # Пустая строка

   assert string_Utils.contains('abc', '') is True                    # Пустая подстрока

   assert string_Utils.contains('Sky😁Pro', '😁') is True            # Эмодзи



# Тестирование метода delete_symbol

def test_delete_symbol():

# Позитивные тесты

   assert string_Utils.delete_symbol('SkyPro', 'k') == 'SyPro'         # Удаление символа

   assert string_Utils.delete_symbol('abc123', '123') == 'abc'         # Удаление нескольких символов

   assert string_Utils.delete_symbol('Sky😁Pro', '😁') == 'SkyPro'    # Удаление эмодзи

# Негативные тесты

   assert string_Utils.delete_symbol('', 'a') == ''                     # Пустая строка

   assert string_Utils.delete_symbol('SkyPro', 'X') == 'SkyPro'         # Символ не найден



# Тестирование метода starts_with

def test_starts_with():

# Позитивные тесты

   assert string_Utils.starts_with('SkyPro', 'S') is True               # Символ в начале

   assert string_Utils.starts_with('abc', 'a') is True                  # Символ в начале

   assert string_Utils.starts_with('😁abc', '😁') is True              # Эмодзи в начале

# Негативные тесты

   assert string_Utils.starts_with('SkyPro', 'U') is False              # Символ не найден

   assert string_Utils.starts_with('', 'a') is False                    # Пустая строка

   assert string_Utils.starts_with('abc', 'X') is False                 # Символ не найден



# Тестирование метода end_with

def test_end_with():

# Позитивные тесты

   assert string_Utils.end_with('SkyPro', 'o') is True                   # Окончание совпадает

   assert string_Utils.end_with('abc', 'c') is True                      # Окончание совпадает

   assert string_Utils.end_with('abc😁', '😁') is True                  # Окончание совпадает

# Негативные тесты

   assert string_Utils.end_with('SkyPro', 'U') is False                   # Окончание не совпадает

   assert string_Utils.end_with('', 'a') is False                         # Пустая строка

   assert string_Utils.end_with('abc', 'C') is False                      # Окончание не совпадает верхний регистр



# Тестирование метода list_to_string

def test_list_to_string():

# Позитивные тесты

   assert string_Utils.list_to_string(['a', 'b', 'c'], ',') == 'a,b,c'  # Разделитель запятая 

   assert string_Utils.list_to_string(['a', 'b', 'c'], ':') == 'a:b:c'  # Двоеточие разделитель
   
   assert string_Utils.list_to_string(['4 ноября 2024'], ' ') == '4 ноября 2024'  # пробел разделитель

# Негативные тесты

   assert string_Utils.list_to_string(['a', '', 'b', 'c'], ',') == 'a,,b,c'               # Пустые элементы

   assert string_Utils.list_to_string([]) == ''                                           # Пустой список

   assert string_Utils.list_to_string(['a', 'b', 'c'], '') == 'abc'                       # Без разделителя