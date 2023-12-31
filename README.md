# Технологии, используемые в данном проекте:

- Python 3.11
- Django 4.2.4
- Django Rest Framework 3.14
- Djoser 2.2.0
- Docker
- PostgreSQL
- Nginx

# Описание проекта:

Проект позволяет пользователю создавать и редактировать рецепты любимых блюд, в том числе используя большую встроенную базу ингредиентов. Рецепты можно добавлять в избранное и список покупок. Для удобства пользователя, сделана выгрузка ингредиентов всех блюд из списка покупок, с суммированием по ингредиентам. Также имеется возможность подписки на сторонних пользователей, фильтрация по тегам.

Документация по API проекта расположена по адресу `../api/docs/`

# Инструкция:

Для развёртывания проекта на сервере необходимо:

1. Установить на сервер `docker` и `docker-compose`
2. Создать файл `.env` в директории `/infra/`. Для примера в репозитории приведен файл `.env.example`
3. Развернуть контейнеры на сервере командой `docker compose up --build`
4. Выполнить миграции моделей в базу данных командой `docker compose exec backend python manage.py migrate`
5. Собрать статику командой `docker compose exec backend python manage.py collectstatic`
6. Импортировать информацию об игредиентах из вспомогательного файла проекта в основную БД `PostreSQL` командой `docker compose exec backend python manage.py ing_import`
7. Создать суперпользователя для ввода информации о тегах командой `docker compose exec backend python manage.py createsuperuser`
8. На ресурсе `../admin/` войти под созданным по пункту 7 суперпользователем и создать несколько тегов (например "завтрак", "обед", "ужин")
9. Проект готов к применению по назначению!

# Об авторе:

Автор проекта - Зайковский Всеволод.

Email для связи - 4lk4st@gmail.com
