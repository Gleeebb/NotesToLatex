# Install

Для разворачивания приложения на Вашем устройстве будем использоваться **virtualenv**.

Инструкция только для текующего, недоработанного, функционала.

## Установка и настройка **virtualenv**
```bash
sudo pip install virtualenv
virtualenv Notes
source ./myapp/bin/activate
cd ./myapp
```

## Загрузка репозитория
```bash
git clone https://github.com/ttgadaev/NotesToLatex/
cd ./NotesToLatex
```

## Установка необходимых пакетов
```bash
pip install django
pip install django-bootstrap-form
```

## Настройка приложения
```bash
cd ./src/django_site/
python manage.py makemigrations
python manage.py migrate
```

Все подготовитьельные работы выполненны, можно запустить приложение. 

## Запуск приложения
```bash
python manage.py runserver
```



