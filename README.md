# DeliniTime - Cafe

## Опис проєкту:  
**Сайт-кафе надає можливість:**

- бронювання столиків  
- перегляд меню  
- додавання замовлень у кошик з підтвердженням через пошту  
- можливість залишати відгуки  
- реєстрація та авторизація  

## Технології:

- Python  
- Django  
- Django ORM  
- PostgreSQL  
- Docker  
- Bootstrap (шаблон)  
- трохи JavaScript (для інтерфейсу)  

## Встановлення та запуск:

1. Клонувати репозиторій:

- git clone https://github.com/QertySX/DeliniTimeCafe.git  

2. Створити віртуальне середовище та встановити залежності:

- python -m venv venv  
- source venv/bin/activate # для Linux/Mac  
- venv\Scripts\activate # для Windows  
- pip install -r requirements.txt  

3. Створити .env та додати такі параметри

- DB_HOST=host.docker.internal
- DB_PORT=5432
- DB_NAME="ваші дані"
- DB_USER="ваші дані"
- DB_PASSWORD="ваші дані"
- DJANGO_SECRET_KEY="ваш секретний ключ"

3. **Збірка та запуск**:  

- Перейти в папку проєкту - cd root  
- docker-compose up --build  

- Доступно за адресою *http://localhost:8000*  

## Example:

Головна сторінка сайту:  
![Головна сторінка](root/screenshots/1.png)  
![Головна сторінка](root/screenshots/2.png)  

Сторінка меню:  
![Меню](root/screenshots/3.png)  

Сторінка меню для доставки:  
![Меню для доставки](root/screenshots/4.png)  

Сторінка About Us:  
![about us](root/screenshots/5.png)  

Сторінка бронювання столика:  
![Бронювання столика](root/screenshots/6.png)  

Кошик замовлень:  
![Кошик](root/screenshots/8.png)  

Більше скріншотів у папці "screenshots".

