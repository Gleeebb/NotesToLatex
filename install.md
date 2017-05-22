# Install

Для разворачивания приложения на Вашем устройстве будем использоваться **virtualenv**.

Инструкция только для текующего, недоработанного, функционала.

## Установка и настройка **virtualenv**
```bash
sudo pip install virtualenv
virtualenv Notes
source ./Notes/bin/activate
cd ./Notes
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
pip install django-tinymce4-lite
pip install pytesseract

```

## Установка средства распознавания текста
```bash
sudo apt-get install tesseract-ocr
wget https://github.com/tesseract-ocr/tessdata/raw/master/rus.traineddata
mv "rus.traineddata" "ru.traineddata"
sudo mv -v ru.traineddata /usr/share/tesseract-ocr/tessdata
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



