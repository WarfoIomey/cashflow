# cashflow
## Демо-версия проекта на сайте Pythoanywhere

[cashlfow](https://warfolomey.pythonanywhere.com/)

## Стек технологий
- Python 3.9
- Django 3.2.16
- Bootstrap5~
- SQLite3
- HTML
- JavaScripts
## Описание проекта:

**cashflow** - Веб сервис для управления движением денежных средств (ДДС)

**ДДС** - ДДС (движение денежных средств) — это процесс учета, управления и анализа поступлений и списаний денежных средств компании или частного лица. В рамках данного задания пользователь должен иметь возможность вести учет всех денежных операций.

**Возможности приложения**
____

- Создание записи  о движение денежных средств (ДДС):
  - Поля:
    - Дата создания записи - заполняется автоматически, но может быть изменена вручную. Пример записи - 01.01.2025
    - Статус - имеет следующие значения:

        - Бизнес
        - Личное
        - Налог
        - Данный список имеет возможность расширяться
    - Тип - имеет следующие значения:
      - Пополнения
      - Списание
      - Данный список имеет возможность расширяться
    - Категория и подкатегория - пример значений:
      - Категория "Инфраструктура" (подкатегории: "VPS", "Proxy")
      - Категория “Маркетинг” (подкатегории: "Farpost", "Avito")
      - Данный список имеет возможность расширяться
    - Сумма - количество средств в рублях, например, 1 000 рублей.
    - Комментарий - комментарий к записи в свободной форме (необязательный к заполнению).
- Просмотр списка всех записей:
  - Вывод таблицы с данными: дата, статус, тип, категория, подкатегория, сумма, комментарий.
  - Поддержка фильтрации  по дате (с указанием периода дат), статуса, типу, категории, подкатегории.
- Редактирование записи:
  - Возможность изменить любую запись.
- Удаление записи:
  - Возможность удалить любую запись.
- Управление справочниками:
  - Добавление, редактирование и удаление статусов, типов, категорий и подкатегорий.
- Логические зависимости:
  - Подкатегории привязаны к категориям.
  - Категории привязаны к типам. Например, в тип "Списание" относится категория "Маркетинг", в которую входят подкатегории "Farpost", "Avito".

## Инструкция по запуску проекта

1. Клонировать репозиторий:
```
git clone https://github.com/WarfoIomey/cashflow.git
```
2. Перейдите в директорию проекта:
```
cd cashflow
```
3. Создайте виртуальное окружение:
```
python -m venv env
```
4. Активируйте виртуальное окружение:
```
source venv/Scripts/activate
```
5. Установите зависимости из фалй requirements.txt
```
pip install -r requirements.txt
```
6. Перейдите в директорию dss:
```
cd dss
```
7. Создайте миграцию:
```
python manage.py makemigrations
```
8. Выполните миграцию:
```
python manage.py migrate
```
9. (Опционально) Загрузите заготованные данные из файла db.json в базу данных:

  Учетная запись для входа
    - Логин: kirill
    - Пароль: test124578
```
python manage.py loaddata db.json
```
10.  Запустите проект
```
python manage.py runserver
```
## Интерфейс проекта

![spisok-zapisey](![alt text](image.png))
![Подробнее-записи](![alt text](image-1.png))
![форма-создания-записи](![alt text](image-4.png))
![Справочник-список-типов](![alt text](image-2.png))
![Справочник-список-статусов](![alt text](image-3.png))
![Справочник-форма-создания-статуса](![alt text](image-5.png))
![Справочник-форма-создания-типа](![alt text](image-6.png))
![Справочник-подробный-вывод-типа](![alt text](image-7.png))
![Справочник-форма-создания-категории](![alt text](image-8.png))
![Справочник-Форма-редактирования-типа](![alt text](image-9.png))
![Справочник-Форма-удаления-типа](![alt text](image-10.png))
![Справочник-подробный-вывод-категории](![alt text](image-11.png))
![Справочник-форма-создания-подкатегории](![alt text](image-12.png))
![Справочник-форма-редактирования-категории](![alt text](image-13.png))
![Справочник-форма-удаление-категории](![alt text](image-14.png))
![Справочник-вывод-подкатегорий](![alt text](image-15.png))
![Справочник-форма-редактирования-подкатегории](![alt text](image-16.png))
![Справочник-форма-удаления-подкатегории](![alt text](image-17.png))
![Форма-входа](![alt text](image-19.png))
![Форма-регистрации](![alt text](image-20.png))