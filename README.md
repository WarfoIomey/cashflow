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
1. Список записей
![список-записей](/screenshot/image.png)
2. Подробная запись
![Подробнее-записи](/screenshot/image-1.png)
3. Форма создания записи
![форма-создания-записи](/screenshot/image-4.png)
4. Справочник (отображение всех типов)
![Справочник-список-типов](/screenshot/image-2.png)
5. Справочник (отображение всех статусов)
![Справочник-список-статусов](/screenshot/image-3.png)
6. Справочник (форма создания статуса)
![Справочник-форма-создания-статуса](/screenshot/image-5.png)
7. Справочник (форма создания типа)
![Справочник-форма-создания-типа](/screenshot/image-6.png)
8. Справочник (подробный тип)
![Справочник-подробный-вывод-типа](/screenshot/image-7.png)
9. Справочник (форма создания категории)
![Справочник-форма-создания-категории](/screenshot/image-8.png)
10. Справочник (форма редактирования типа)
![Справочник-Форма-редактирования-типа](/screenshot/image-9.png)
11. Справочник (форма удаления типа)
![Справочник-Форма-удаления-типа]((/screenshot/image-10.png))
12. Справочник (подробная категория)
![Справочник-подробный-вывод-категории](/screenshot/image-11.png)
13. Справочник (форма создания подкатегории)
![Справочник-форма-создания-подкатегории](/screenshot/image-12.png)
14. Справочник (форма редактирования категории)
![Справочник-форма-редактирования-категории](/screenshot/image-13.png)
15. Справочник (форма удаления категории)
![Справочник-форма-удаление-категории](/screenshot/image-14.png)
16. Справочник (подробный вывод подкатегории)
![Справочник-вывод-подкатегорий](/screenshot/image-15.png)
17. Справочник (форма редактирования подкатегории)
![Справочник-форма-редактирования-подкатегории](/screenshot/image-16.png)
18. Справочник (форма удаления подкатегории)
![Справочник-форма-удаления-подкатегории](/screenshot/image-17.png)
19. Форма входа
![Форма-входа](/screenshot/image-19.png)
20. Форма регистрации
![Форма-регистрации](/screenshot/image-20.png)