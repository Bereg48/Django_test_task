# Тестовое Django-приложение.

## Предназначение приложения:
...

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
    Команда для Windows:
        1- python -m venv venv
        2- venv\Scripts\activate
        3- pip install -r requirements.txt

    Команда для Unix:
        1- python3 -m venv venv
        2- source venv/bin/activate 
        3- pip install -r requirements.txt

### 2. Для работы с переменными окружениями необходимо заполнить файл
    - .env

### 3. Для запуска приложения: 
    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver

### 4. Для наполнения базы из файла utils.py необходимо пройти по пути: 
    http://127.0.0.1:8000/load_data/

### 5. Для отображения страницы продуктов необходимо пройти по пути: 
    http://127.0.0.1:8000/products/

