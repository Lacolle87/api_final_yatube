
# Yatube API

## Описание
Данный проект предоставляет доступ к сервису Yatube 
посредством API. 
Он позволяет запрашивать данные о постах, 
группах, комментариях в социальной сети Yatube, 
а также создавать новые.

## Технологии
- Python
- Django
- Django REST Framework (DRF)
- SQLite3
- Git

## Как запустить проект
1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/DOSuzer/api_final_yatube.git
cd api_final_yatube
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv env
source env/bin/activate
```

3. Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполните миграции:

```
python manage.py migrate
```

5. Запустите проект:

```
python manage.py runserver
```
## Подробная документация по работе API:

```
http://127.0.0.1:8000/redoc/
```

## Примеры взаимодействия
Вам доступны следующие эндпойнты:

- `api/v1/posts/` - список всех постов
- `api/v1/groups/` - список всех групп
- `api/v1/posts/<post_id>/comments/` - список всех комментариев к посту (где `<post_id>` - номер поста)
- `api/v1/follow/` - список всех подписок (только для авторизованных пользователей)

**Пример публикации поста (POST запрос к `api/v1/posts/`):**

```json
{
    "text": "Пост!"
}
```

**Пример редактирования поста (PATCH запрос к `api/v1/posts/<post_id>/`):**

```json
{
    "text": "Текст!",
    "group": 1
}
```

**Пример добавления комментария (POST запрос к `api/v1/posts/<post_id>/comments/`):**

```json
{
    "text": "Комментарий!"
}
```

**Пример подписки на автора (POST запрос к `api/v1/follow/`):**

```json
{
    "following": "user1"
}
```

## Автор
Автор проекта - Никита Кузнецов, студент Яндекс.Практикум.

GitHub: https://github.com/Lacolle87