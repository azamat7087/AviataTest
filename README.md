# AviataTest

## 1. Запустить provider-a с помощью команды docker-compose build app и docker-compose up
## 2. Запустить provider-b с помощью команды docker-compose build app и docker-compose up
## 3. Запустить airflow с помощью команды docker-compose build app и docker-compose up
## 4. Зайти в bash с помощью команды docker exec -it airflow
## 5. Провести миграции python manage.py migrate
## 6. Добавить таски к крону с помощью команды python manage.py crontab add
## 7. В директории airflow, в файле .env изменить LOCAL_IP на локальный адрес машины
## 8. Отправить POST запрос на адрес http://0.0.0.0:9000/search/
## 9. Отправить GET запрос на адрес http://0.0.0.0:9000/results/{search_id}/{currency}
