# Install

Для разворачивания приложения на Вашем устройстве будем использоваться **virtualenv**.
Пока что только для текущего функционала.

## Установка и настройка **virtualenv**
```bash
sudo pip install virtualenv
virtualend Notes
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

## Запусе приложения
```bash
python manage.py runserver
```



