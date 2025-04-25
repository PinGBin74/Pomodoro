# Pomodoro Time - API для управления задачами

## Описание проекта
Pomodoro Time - это REST API сервис для управления задачами, построенный на FastAPI. Проект реализует функционал для создания, обновления, удаления и получения списка задач с поддержкой аутентификации пользователей.

## Технологии
- FastAPI
- PostgreSQL
- Docker
- Poetry (управление зависимостями)
- Alembic (миграции базы данных)
- Gunicorn
- Sentry (мониторинг ошибок)

## Структура проекта
```
.
├── app/                    # Основной код приложения
│   ├── tasks/             # Модуль задач
│   ├── users/             # Модуль пользователей
│   ├── broker/            # Модуль для работы с брокером сообщений
│   └── infrastructure/    # Инфраструктурный код
├── tests/                 # Тесты
├── alembic/               # Миграции базы данных
├── docker-compose.yml     # Конфигурация Docker Compose
├── Dockerfile            # Конфигурация Docker
└── pyproject.toml        # Зависимости проекта
```

## API Endpoints

### Задачи
- `GET /task/all` - Получить список всех задач
- `POST /task/` - Создать новую задачу
- `PATCH /task/{task_id}` - Обновить название задачи
- `DELETE /task/{task_id}` - Удалить задачу

### Пользователи
- `POST /auth/register` - Регистрация нового пользователя
- `POST /auth/login` - Аутентификация пользователя
- `GET /user/profile` - Получить профиль пользователя

## Установка и запуск

### Локальная разработка

1. Установите Poetry:
```bash
pip install poetry
```

2. Установите зависимости:
```bash
poetry install
```

3. Создайте файл `.local.env` с необходимыми переменными окружения:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
```

4. Примените миграции:
```bash
alembic upgrade head
```

5. Запустите приложение:
```bash
poetry run uvicorn app.main:app --reload
```

### Docker

1. Соберите и запустите контейнеры:
```bash
docker-compose up --build
```

## Тестирование

Для запуска тестов:
```bash
poetry run pytest
```

## CI/CD

Проект настроен с использованием GitHub Actions для автоматического тестирования и деплоя.

## Мониторинг

Проект интегрирован с Sentry для мониторинга ошибок и производительности.

