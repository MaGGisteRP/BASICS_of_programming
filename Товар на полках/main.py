import pickle

# Считываем данные из текстового файла
data = []
with open('input.txt', 'r') as file:
    for line in file:
        name, price, is_on_sale = line.strip().split()
        price = int(price)
        is_on_sale = bool(int(is_on_sale))
        data.append((name, price, is_on_sale))

# Сортируем данные по названию продукта в алфавитном порядке
data.sort(key=lambda x: x[0])

# Записываем данные в новый текстовый файл
with open('output1.txt', 'w') as file:
    for item in data:
        file.write(f"{item[0]} {item[1]} {int(item[2])}\n")

# Записываем данные в новый бинарный файл
with open('output2.bin', 'wb') as file:
    pickle.dump(data, file)

# Считываем данных из двоичного файла
with open('output2.bin', 'rb') as file:
    data = pickle.load(file)

# Сортируем данные по цене в порядке возрастания
data.sort(key=lambda x: x[1])

# Записываем данные в новый текстовый файл
with open('output3.txt', 'w') as file:
    for item in data:
        file.write(f"{item[0]} {item[1]} {int(item[2])}\n")