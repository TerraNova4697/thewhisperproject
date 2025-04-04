# Настройка и запуск проекта с Kafka и PostgreSQL

## Шаги настройки

1. Переименовать файл примера переменных окружения Kafka:
   ```sh
   mv kafka/env_example kafka/.env
   ```
2. Переименовать файл примера переменных окружения PostgreSQL:
   ```sh
   mv postgres/env_example postgres/.env
   ```
3. Настроить переменные окружения для Kafka в файле `kafka/.env`.
4. Настроить переменные окружения для PostgreSQL в файле `postgres/.env`.
5. Запустить контейнеры с помощью Docker Compose:
   ```sh
   docker compose up -d