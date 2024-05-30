# Инструкция

Этот проект представляет собой простой REST API для управления данными о рейсах с использованием FastAPI и MySQL.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/hexvel/flight-api.git
   cd flight-api
   ```

2. Создайте виртуальное окружение и установите зависимости:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Настройте параметры вашей базы данных MySQL в `app/config.py`.

4. Запустите скрипт миграции базы данных:

   ```bash
   python migrations/create_flights_table.py
   ```

5. Запустите приложение FastAPI:

   ```bash
   uvicorn main:app --reload
   ```

## API Эндпоинты

- `POST /api/v1/flights`: Добавить новый рейс.
- `GET /api/v1/flights/{flight_no}`: Получить информацию о рейсе по его номеру.

## Аутентификация

Используйте заголовок `X-API-KEY: secret` для аутентификации запросов.

## Запуск тестов

Запустите тесты с помощью следующей команды:

```bash
python -m unittest discover tests
```
