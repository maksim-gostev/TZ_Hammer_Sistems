# Тестовое задание для Python разработчика: Hammer Systems

# Стек технологий

- [Python 3.10](https://www.python.org/)
- [Django 4.2.2](https://www.djangoproject.com/)
- [Django REST Framework 3.14.0](https://www.django-rest-framework.org/)
- [Poetry](https://python-poetry.org/)
- [drf-spectacular](https://pypi.org/project/drf-spectacular/)

### Функционал
#### Django Templates

>* Авторизация по номеру телефона: http://127.0.0.1:8000/user/
 Запрос на ввод номера. Имитирует отправку 4хзначного кода авторизации(задержку
на сервере 1-2 сек).Если пользователя с таким номером телефона нет то создаёт его.
>####
> * Второй запрос на ввод 4хзначного кода авторизации: http://127.0.0.1:8000/user/auth/1/
> ####
> * Профиль пользователя: http://127.0.0.1:8000/user/deteil/1/
> При первой авторизации рандомно сгенерируеться 6-значный инвайт-код(цифры и символы).
> В профиле у пользователя есть возможность ввести чужой
инвайт-код (при вводе проверять на существование). В своем профиле
можно активировать только 1 инвайт код, если пользователь уже когда-
то активировал инвайт код, то выводит его в соответсвующем
поле в запросе на профиль пользователя. Выводиться список пользователей (номеров
телефона), которые ввели инвайт код текущего пользователя.

#### API
>* Авторизация по номеру телефона: 
```html
POST: http://127.0.0.1:8000/api_user/create/
```
Пример ввода:
```json
 {
    "phone": "+79096869722"
 }
```
>* Второй запрос на ввод 4хзначного кода авторизации: 
```html
POST: http://127.0.0.1:8000/api_user/auth/1/
```
Пример ввода:
```json 
{
    "auth_number": 8917
}
```
Пример вывода:
```json  
{
    "token": "46d7112273cc6af7570c01b001fa619a26333da9"
}
```
>* Профиль пользователя: 
```html
GET: http://127.0.0.1:8000/api_user/user/1/
```
>* В Headers :
> Authorization = Token 46d7112273cc6af7570c01b001fa619a26333da9
Пример вывода:
```json
{
    "id": 1,
    "invite_code": "gPcRwV",
    "phone": "+79096869722",
    "invite_user": [
        {
            "phone": "+7(909)686-97-22"
        },
        {
            "phone": "+7(909)686-97-23"
        }
    ]
}
```
>* Активация инвайт кода:
```html
PATCH: http://127.0.0.1:8000/api_user/user/1/
```
Пример вывода:
```json  
{
    "stranger_invite_code": "TwXK36"
}
```


## Подготовка к запуску
>* pip install poetry
>* poetry install
>* python manage.py migrate
>* python manage.py runserver