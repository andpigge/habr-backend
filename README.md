# Кошачий благотворительный фонд. Открытое (API)

### Фонд собирает пожертвования на различные целевые проекты.

**В API существует 2 модели:**
- Благотворительный проект нуждающийся в пожертвовании '/charity_project/'.<br/>
Просмотр всех проектов доступно всем пользователям.<br/>
Операции POST, DELETE, PUTH - доступны только суперпользователю.

- И сами пожертвования '/donation/'.<br/>
Задонатить может авторизированный пользователь.<br/>
Просмотр всех пожертвований и их редактирование доступно только суперпользователю.

Для проекта установлена дополнительная валидация:
- Если в проекте были внесены средства, он не подлежит удалению.
- Закрытый проект нельзя редактировать.
- Нельзя установить сумму меньше уже внесенной суммы в проект.

Реализован service который подключается в случае создание проекта или доната:
- Если необходимая сумма пожертвования меньше от суммы необходимой, то донат считается закрытым.
- Если доступная сумма пожертвования равна от необходимой, то донат и проект считаетются закрытыми.
- Если доступная сумма пожертвования больше от суммы необходимой, то проект считается закрытым.

**И 2 категории с аутентификацией и просмотр пользователя, со стандартным набором библиотеки FastAPI Users**
- auth (регистрация, создание токена, и выход)
- users (просмотр и изменения профиля, просмотр пользователя и изменения пользователя по id.)
Просмотр своего профиля и редоктирование доступно авторизированым пользователям.
Просмотр чужого профиля по id и редактирование чужого профиля доступно только суперпользователю.

<h2 align="center">Технологии</h2>

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
<a href="https://fastapi-users.github.io/fastapi-users/11.0/" target="_blank"><img src="https://raw.githubusercontent.com/fastapi-users/fastapi-users/master/logo.svg" height="20" /></a>
<a href="https://www.sqlalchemy.org/" target="_blank"><img src="https://www.sqlalchemy.org/img/sqla_logo.png" height="28" /></a>

<a href="https://alembic.sqlalchemy.org/en/latest/" target="_blank">Alembic</a> - для миграций БД sqlalchemy.<br/>
<a href="https://github.com/pycqa/flake8" target="_blank">flake8</a> - для соблюдения стандарта кода pep8.

<h2 align="center">Примеры API</h2>

<table>
<thead>
    <tr>
        <th colspan="2">Пользователи</th>
    </tr>
</thead>

<tr>
<td>
    <p align="center"><ins>/users/me</ins> - GET</p>
</td>

<td>
  <p align="center"><ins>/users/me</ins> - PUTCH</p>
    <p>
        <strong>body:</strong> {<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;"id": "string",<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;"email": "user@example.com",<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;"is_active": true,<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;"is_superuser": false,<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;"is_verified": false
        <br/>{
    </p>
</td>
</tr>

<tr>
<td valign="top">
          
    {
      "id": "string",
      "email": "user@example.com",
      "is_active": true,
      "is_superuser": false,
      "is_verified": false
    }
        
</td>

<td valign="top">

    {
      "id": "string",
      "email": "user@example.com",
      "is_active": true,
      "is_superuser": false,
      "is_verified": false
    }

</td>
</tr>
  
<thead>
<tr>
  <th colspan="2">
    Благотворительный проект
  </th>
</tr>
</thead>
  
<tr>
<td>
    <p align="center"><ins>/charity_project/</ins> - GET (Все благотворительные проекты)</p>
</td>

<td>
  <p align="center"><ins>/charity_project/</ins> - POST</p>
  <p>
      <strong>body:</strong> {<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"name": "Вкусный корм",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"description": "Вкусный корм фирмы 'Кис-Кис-Мяу'",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"full_amount": 2000
      <br/>}
  </p>
</td>
</tr>

<tr>
<td valign="top">

    [
      {
        "name": "Вкусный корм",
        "description": "Вкусный корм фирмы 'Кис-Кис-Мяу'",
        "full_amount": 2000,
        "id": 1,
        "invested_amount": 0,
        "fully_invested": true,
        "create_date": "2023-05-27T17:46:29.841Z",
        "close_date": "2023-05-27T17:46:29.841Z"
      }
    ]

</td>
  
<td valign="top">

    {
      "name": "Вкусный корм",
      "description": "Вкусный корм фирмы 'Кис-Кис-Мяу'",
      "full_amount": 2000,
      "id": 1,
      "invested_amount": 0,
      "fully_invested": true,
      "create_date": "2023-05-27T17:47:29.377Z",
      "close_date": "2023-05-27T17:47:29.377Z"
    }
 
</td>

<tr>
<td>
    <p align="center"><ins>/charity_project/{project_id}</ins> - DELETE</p>
</td>

<td>
    <p align="center"><ins align="center">/charity_project/{project_id}</ins> - PUTCH</p>
    <p>
        <strong>body:</strong> {<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;"name": "Вкусный корм",<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;"description": "Вкусный корм фирмы 'Кис-Кис-Мяу'",<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;"full_amount": 2000
        <br/>}
    </p>
</td>
</tr>

<tr>
<td valign="top" colspan="2">

    {
      "name": "Вкусный корм",
      "description": "Вкусный корм фирмы 'Кис-Кис-Мяу'",
      "full_amount": 2000,
      "id": 1,
      "invested_amount": 0,
      "fully_invested": true,
      "create_date": "2023-05-27T17:47:29.377Z",
      "close_date": "2023-05-27T17:47:29.377Z"
    }
 
</td>
</tr>
  
<thead>
<tr>
  <th colspan="2">
    Пожертвования
  </th>
</tr>

<tr>
<td>
    <p align="center"><ins>/donation/</ins> - GET (Все пожертвования)</p>
</td>

<td>
    <p align="center"><ins>/donation/my/</ins> - GET (Мои пожертвования)</p>
</td>
</tr>

<tr>
<td valign="top">

    [
      {
        "full_amount": 2000,
        "comment": "string",
        "id": 1,
        "user_id": 0,
        "invested_amount": 0,
        "fully_invested": true,
        "create_date": "2023-05-27T18:07:35.574Z",
        "close_date": "2023-05-27T18:07:35.574Z"
        }
     ]

</td>
  
<td valign="top">

    [
      {
        "full_amount": 2000,
        "comment": "string",
        "id": 1,
        "create_date": "2023-05-27T18:07:35.567Z"
      }
    ]

</td>
</tr>

<tr>
<td>
  <p align="center"><ins>/donation/</ins> - POST</p>
  <p>
      <strong>body:</strong> {<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"full_amount": 2000,<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"comment": "string"
      <br/>}
  </p>
</td>
</tr>
  
<tr>
<td valign="top">

    {
      "full_amount": 2000,
      "comment": "string",
      "id": 1,
      "create_date": "2023-05-27T18:09:51.288Z"
    }

</td>
</tr>
</thead>
<table>

<h2 align="center">Процесс запуска приложения</h2>
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/andpigge/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить приложение

```
uvicorn app.main:app --reload

где:
- uvicorn - асинхронный сервер
- app.main:app - пусть к приложению запуска
- --reload - обновление сервера при каждом изменении в коде
```

Основные команды алембика (миграции) описаны здесь:
https://github.com/andpigge/cat_charity_fund/tree/master/alembic#readme

<h2 align="center">.env</h2>

Содержимое env-файла (для просмотра приложения .env файл создавать не обязательно)

```
APP_TITLE=Фонд QRKot
APP_DESCRIPTION=API для фонда сбора пожертвования на различные целевые проекты нуждающихся хвостатым.
SECRET=f2d07fea-c0d7-40d2-a092-c946cc52e26e
```
SECRET - Ваш секретный ключ. В приложении он индивидуален.

<h2 align="center">Информация об авторе</h2>
<table align="center">
  <tbody>
    <tr>
      <td align="center" valign="top" height="400">
        <img width="200" height="200" src="https://avatars.githubusercontent.com/u/54473049?v=4?s=200">
        <br>
        <a href="https://github.com/andpigge">Рустам Рахимов</a>
        <p></p>
        <a href="https://hh.ru/resume/dc361442ff07787a170039ed1f314a4e42476c">
          <img height="30px" src="https://i.hh.ru/logos/svg/hh.ru__min_.svg?v=11032019">
        </a>
        <br>
        <p>python-developer</p>
        (подтвержденной информации не имеется)
      </td>
    <tr>
  <tbody>
<table>
