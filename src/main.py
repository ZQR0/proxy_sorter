import glob

proxies = glob.glob('src/proxies.txt')

#Итерируемся по проксям
for items in proxies:
    #Открываем файл с проксями на чтение
    with open(items, mode='r', encoding='utf-8') as file:
        #Читаем по линиям
        lines = file.readlines()

        #Итерируемся по линиям
        for line in lines:
            deb = '=' * 12

            line_index = lines.index(line)

            proxy = lines[line_index]

            #записываем в новый файл отсортированные прокси
            with open('src/sorted.txt', mode='a', encoding='utf-8') as new_file:
                new_file.write(f'{deb}\n{proxy}\n{deb}')