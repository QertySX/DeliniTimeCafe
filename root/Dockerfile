FROM python:3.11

WORKDIR /app

# Копируем только requirements.txt сначала
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код проекта
COPY . .

# Сбор статики
RUN python manage.py collectstatic --noinput

# Запуск через gunicorn 
CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]

RUN apt-get update && apt-get install -y postgresql-client
