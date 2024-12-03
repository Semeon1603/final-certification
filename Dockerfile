FROM python:3.12.7-slim
# Устанавливаем рабочую директорию в базовом образе для команд COPY, RUN, ENTRYPOINT и CMD
WORKDIR /app
# Копируем с хоста в образ файл с требуемыми зависимостями
COPY requirements.txt ./
# Устанавливаем зависимости внутри образа
RUN pip install --no-cache-dir -r requirements.txt
# Переменные окружения
ENV NAME='Bob'
ENV PYTHONPATH=E:/docker_python_app
# Копируем код приложения в контейнер, одновременно выставляя нужные разрешения
COPY app.py ./
# Задаем команду, которая будет запускаться при старте контейнера
ENTRYPOINT [ "python" ]
# Задаем аргументы по умолчанию для команды в ENTRYPOINT
CMD [ "app.py"]