# cashflow
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/WarfoIomey/cashflow.git`

`cd cashflow`

Cоздать и активировать виртуальное окружение:

`python -m venv env`

`source venv/Scripts/activate`

Установите зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Перейдите в папку dss:

`cd dss`

Выполнить миграции:

`python manage.makemigrations`

`python manage.py migrate`

Загрузите данные из файла db.json в базу данных:

`python manage.py loaddata db.json`

Запустить проект:

`python manage.py runserver`

Логин пользователя для тестов

Username = kirill

Password = test124578
