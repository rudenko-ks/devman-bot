# Отправляем в Telegram уведомления о проверке работ на сайте devman.org

Long Polling клиент для сервиса проверки работ образовательного сайта [devman.org](https://dvmn.org/modules/). Отправляет запрос на сайт и ожидает получение статуса проверки. Получим ответ от сервиса, уведомляет о статусе проверенной работы, отправив сообщение пользователю в мессенджер Telegram.

<p align="center">
  <img src="https://user-images.githubusercontent.com/3808020/215220128-f3f15218-a47a-4d5e-945b-1b392a2c83c5.png" />
</p>

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге вашего приложения (рядом с `main.py`) и запишите туда данные в формате `ПЕРЕМЕННАЯ=значение`.

- `DEVMAN_TOKEN`  —  персональный токен пользователя на сайте
- `TELEGRAM_CHAT_ID`  — уникальный идентификатор пользователя в мессенджере Telegram
- `TELEGRAM_BOT_API_TOKEN`  — персональный токен Telegram бота 

Пример содержимого `.env` файла:
```
DEVMAN_TOKEN  = eAwn0sZ1?AgFZpCa3O-Pyt9QPk8L92vwRkgC!3WpaJao34
TELEGRAM_CHAT_ID  = 123456789
TELEGRAM_BOT_API_TOKEN  = lCwAKB4BXlWDnVYWPF?DsoOlRoUx!skWdkXCN6Qu
```

## Установка

- Клонируйте репозиторий с Github:
```shell
https://github.com/rudenko-ks/devman-bot.git
```
- Создайте виртуальное окружение:
```shell
python -m venv .venv
source .venv/bin/activate
```
- Установите зависимости командой:
```shell
pip install -r requirements.txt
```
## Запуск
- Запустите сервер командой:
```shell
python main.py
```
> Written with [StackEdit](https://stackedit.io/).
