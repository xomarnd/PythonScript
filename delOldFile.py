import os
import datetime
import time

root = os.path.join(DIR)
timeQuotaText = "1 месяц"
timeCoolDown = 60 * 60 * 24 * 31
current_time = time.time()


def serchOldFile (path):
    if os.path.isdir(path):
        print('КАТАЛОГ: ' + path)
        if os.listdir(path):
            print('Список объектов в нем: ', os.listdir(path))
            for whoIs in os.listdir(path):
                a = os.path.join(path, whoIs)
                if os.path.isdir(whoIs):
                    print('Ищем глубже')
                serchOldFile(a)
                if os.path.isdir(a):
                    if not os.listdir(a):
                        if (current_time - os.path.getctime(a)) > timeCoolDown:
                            print('Каталог был пуст и старше ' + timeQuotaText + ' => удален')
                            os.rmdir(a)
                        else:
                            print('Каталог младше ' + timeQuotaText + ':' + time.ctime(os.path.getctime(a)) + '.')

    elif os.path.isfile(path):
        if (current_time - os.path.getatime(path)) > timeCoolDown:
            print('Файл: ' + path + ' удален. Файл не использовали ' + timeQuotaText + '.')
            os.remove(path)
        else:
            print('Файл: ' + path + ' этим файлом пользуются, последний раз:', datetime.datetime.fromtimestamp(int(os.path.getatime(path))))

serchOldFile(root)
