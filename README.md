# bruh

### Локальный билд

1. В `.env` файл добавить данные для подключения к БД
2. `pip install -r requirements.txt`
3. `pip install -e .`
4. `cd src/`
5. `alembic upgrade head`
6. `uvicorn main:app`

### Docker

1. Поменять данные `.env`, если нужен другой порт
2. `docker-compose up`


### Структура
`tests/` - тесты эндпоинтов
`src/` - исходный код
`src/main.py` - файл для запуска, совмещает все роуты в одно приложение
`src/routes/` - эндпоинты для подключения к `main.py`
`src/db/` - подключение к базе данных и CRUD
`src/models` - модели pydantic
`src/alembic/` - миграции
