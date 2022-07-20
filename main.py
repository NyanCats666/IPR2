import gzip
import re

Test = open("TestFileWriter", "w", encoding="utf-8")                                                                    # Создание и открытие файла в нужном формате и с нужной кодировкой
with gzip.open('csv_example.csv.gz', 'rb') as f:                                                                        # Открытие архива
    for i, line in enumerate(f):                                                                                        # Цикл по номерам линий в документе
        print(line)                                                                                                     # Принт для понятия времени текущей линии парсера
        mount = (re.search(r'[A-Z]{1}[a-z]{2}', str(line))).group(0)                                                    # Рега на первое значение месяца
        day = (re.search(r'[0-9]{1}', str(line))).group(0)                                                              # Рега на значение дня
        time = (re.search(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', str(line))).group(0)                                           # Рега на значение времени
        logIn = (re.search(r'[a-z,0-9]{15}', str(line))).group(0)                                                       # Рега на значение то ли логина то ли операции
        prochee = re.sub(r' ', '|', ((re.search(r'esia.gosuslugi.ru_https_access:.*', str(line))).group(0)))            # Рега на значение меняющейся тушки с ресабом на разделение
        Test.write(mount + "|" + day + "|" + time + "|" + logIn + "|" + prochee + '\n')                                 # Запись в нужном формате с переводом строки
Test.close()
print('Успешно!')


# Неиспользованные переменные
        # serName = (re.search(r'esia.gos.*?\s', str(line))).group(0)
        # timeStamp = (re.search(r'[0-9]{2}\/[A-Z]{1}[a-z]{2}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}', str(line))).group(0)
        # lat = (re.search(r'\+[0-9]{4}', str(line))).group(0)
        # ip = (re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(line))).group(0)
        # lat = (re.search(r'\+[0-9]{4}', str(line))).group(0)
        # restMethod = (re.search(r'[A-Z]{4}|[A-Z]{3}', str(line))).group(0)
        # restPath = (re.search(r'\/[a-z].*?\s', str(line))).group(0)
        # HTTPver = (re.search(r'HTTP.*?\s', str(line))).group(0)
        # responceTime = (re.search(r'upst.+?[0-9].+?[0-9].+|upst.+?[0-9].+?[0-9].+?\n|upst.+?\n|upst.+?-', str(line))).group(0)
        # if re.match(r'\\n', responceTime):

# Предыдущий принт (умерший, так как реги на prochee не находит иногда значение)
        # Test.write(mount + "|" + day + "|" + time + "|" + logIn + "|" + serName + "|" + timeStamp + "|" +
        #            lat + "|" + ip + "|" + restMethod + "|" + restPath + "|" + HTTPver + "|" + prochee + "|" + responceTime + '\n')