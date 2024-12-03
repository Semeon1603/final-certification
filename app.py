from pathlib import Path
import os
import datetime

# Передача имени пользователя через переменную окружения docker
value = os.environ.get("NAME")
print(f"Hello, {value}!")
#folder_name = os.environ.get("PYTHONPATH")

dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time: {dt_now}")

#user_name = input("What is your name?")
# Запрос пути
folder_name = input("Specify the path:")
#folder_name = 'E:/docker_python_app'

try:
    list = os.listdir(folder_name) #заданная пользователем папка
except FileNotFoundError:
    path, dirs, files = next(os.walk(os.getcwd())) #корневая папка, если пользователь не задал путь
    folder_name = path
    list = os.listdir(folder_name)

#Подсчет кол-ва файлов в директории
folder = Path(folder_name)
if folder.is_dir():
    folder_count = len([file for file in folder.iterdir() if file.is_file()])
    print(f"Total numbers of files: {folder_count}")

#Сортировка файлов по размеру от большего к меньшему
print("Top 10 largest files:")
pairs = []
for file in list:
    location = os.path.join(folder_name, file)
    size = os.path.getsize(location)
    pairs.append((location, size/1024.0, "Kb"))
pairs.sort(key=lambda s: s[1], reverse= True)

#Вывод топ 10 файлов
i = 0
for pair in pairs:
    if(i<10):
        print (pair)
    i=i+1