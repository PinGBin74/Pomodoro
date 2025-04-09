FROM python:3.12-alpine

# Установка системных зависимостей
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    libffi-dev \
    make \
    git \
    build-base \
    libpng-dev \
    freetype-dev \
    lapack-dev \
    gfortran \
    openblas-dev \
    linux-headers \
    pkgconfig \
    cmake

# Установка рабочей директории
WORKDIR /app

# Копирование всего кода
COPY . /app/

# Установка зависимостей через pip
RUN pip install --no-cache-dir -U pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Добавление /app в PYTHONPATH
ENV PYTHONPATH=/app

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]