# test_ida_image

* test_ida_image

Сервис по работе с Изображениями

### Требования


[Python](https://www.python.org/downloads/) v3.7 +  для запуска.
Установите зависимости и виртуальное окружение и запустите сервер.

```sh
$ pip install virtualenv
$ virtualenv 'название виртуального окружения', либо python3 -m venv 'название виртуального окружения'
$ venv 'название виртуального окружения'/Scripts(или bin для linux)/activate
$ pip install -r requirements.txt
$ python manage.py collectstatic
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Запуск через докер

[Docker](https://www.docker.com/)

Установка для linux
```sh
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
$ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$ (lsb_release -cs) \
$ stable"
$ sudo apt update
$ sudo apt install docker-ce -y
```
После установки выполнить следующие действия:
1. В корневой директории проекта создайте образ командой docker build -t <тут введите имя образа> .
2. Запустите контейнер командой docker run -it -p 8000:8000 <имя образа>
3. Приложение будет доступно в браузере по адресу http://localhost:8000/.

## Доступные url
| [Главная страница](http://127.0.0.1:8000)

| [Загрузка изображения](http://127.0.0.1:8000/upload-image/)

| [Изменение размера изображения](http://127.0.0.1:8000/image/<int:images_id>/)


## Авторы

* **Vladimir Svetlakov** - [svvladimir-ru](https://github.com/svvladimir-ru)