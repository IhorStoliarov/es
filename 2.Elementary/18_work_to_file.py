# відкрити файл в поточній теці в режимі читання в кодуванні UTF-8!!!
file_ovk = open('ovk_choven.txt', encoding="utf-8")
# виводимо інфу про нього
print(file_ovk)

# вивести вміст файла і закрити його
data = file_ovk.read()
print(data)
file_ovk.close()
