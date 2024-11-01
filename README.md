# Описание проекта

## Основной Стэк : (FastAPI, SQLAlchemy , Alembic)

## Описание проекта:
### ▎Описание директорий проекта

▎Структура проекта

src/
├── config/
│   ├──                   **Файлы настроек для переменных окружения и подключения к БД**

├── database/

  │   ├── postgres/
  
│   │   ├── base/         **Файл с созданием подключения к PostgreSQL и сессий**

│   │   └── tables/       **Описание таблиц базы данных PostgreSQL**

│   └── redis/            **Файл с подключением к Redis**

├── dependencies/         **Файл для реализации паттерна Dependency Injection**

├── repositories/

│   ├── redis/

│   │   ├── referrals/

│   │   │   ├── base.py        **Абстрактный класс для репозитория рефералов**

│   │   │   └── referrals.py   **Реализация репозитория рефералов**

│   │   └── user/

│   │       ├── base.py    **Абстрактный класс для репозитория пользователей**

│   │       └── user.py   **Реализация репозитория пользователей**

├── routing/

│   ├── auth/          **Слой роутинга для аутентификации**

│   ├── refer/         **Слой роутинга для рефералов**

│   └── user/          **Слой роутинга для пользователей**

├── schemas/

│   ├── base.py        **Абстрактные классы DTO**

│   └── schemas.py     **Реализация схем DTO**

├── services/

│   └── user/

│       └── user.py  **Бизнес-логика приложения**


└── utils/
    
  └── jwt.py   **Логика создания и проверки JWT**



▎Описание директорий

• src/config/: Содержит файлы настроек, которые отвечают за подтягивание переменных окружения и создание подключения к базе данных.

• src/database/: В этой директории хранятся подкаталоги для работы с различными базами данных.

  • postgres/: 

    • base/: Файл для создания подключения к базе данных PostgreSQL и управления сессиями.

    • tables/: Описание таблиц базы данных PostgreSQL.

  • redis/: Файл с реализацией подключения к Redis.

• src/dependencies/: Реализация паттерна Dependency Injection, который упрощает управление зависимостями в приложении.

• src/repositories/: Содержит директории для работы с репозиториями.

  • redis/: 

    • referrals/: 

      • base.py: Абстрактный класс для репозитория рефералов.

      • referrals.py: Реализация репозитория рефералов.

    • user/: 

      • base.py: Абстрактный класс для репозитория пользователей.

      • user.py: Реализация репозитория пользователей.

• src/routing/: Слой роутинга приложения, разделенный на директории:

  • auth/: Роуты для аутентификации.

  • refer/: Роуты для рефералов.

  • user/: Роуты для пользователей.

• src/schemas/: Содержит абстрактные классы DTO и их реализацию.

  • base.py: Абстрактные классы DTO.

  • schemas.py: Реализация схем DTO.

• src/services/: Реализация бизнес-логики приложения.

  • user/user.py: Основной файл, в котором реализована бизнес-логика и используется UserService, применяя созданные репозитории.

• src/utils/: Утилитарные функции, включая логику создания и проверки JWT. 

## Инструкции к запуску: 
 -**Создать файл .env , скопировать в него содержимое .env.example**.
 
 -**Запустить контейнеры с помощью команды docker compose up**.

## Инструкции к тестированию: 
  ### Эндопинты для тестирования работоспособности:
  -**"/users/create"** - Эндпоинт для создания юзера, принимает в себя параметры (username: str , password : str, email: str , referals - str | None)
  
  -**"/users/getcode"** - Эндпоинт для получения кода по почте юзера, принимает в себя параметр(email: str)
  
  -**"/users/getref/{}"** - Эндпоинт для получения информации о рефералах по id их реферала , принимает в себя параметр пути с указанием id т.е /users/getref/1
  
  -**"/referal/create"** - Эндпоинт для создания реферального кода, принимает в себя один параметр(code: str) , работает только с авторизированным пользователями
  
  -**"/referal/delete"** - Эндпоинт для удаления реферального кода, не принимает параметров, работает только с авторизированным пользователями, из jwt токена получает id юзера для удаления кода
  
  -**"/auth/login"** - Эндпоинт для авторизации, принимает в себя два параметра(username: str, password: str) , возвращает Response сохраняя в куках jwt токен
  
