For execute this project 

Make sure you have pythons libraries :
-daphne
-channels 

python manage.py runserver                  #for django server
daphne -p 1999 chatDjango.asgi:application  #for websocket server

