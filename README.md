python -m venv venv
venv/Scripts/activate

pip install -r requirements.txt

Создать файл .env
SECRET="6a0kj6z06h2(m$*)111_-(tq2_c+^+^k$&=8w8*s4r9*8j6v+h"

python manage.py migrate

python manage.py createsuperuser --username admin --email admin@domain.com

python manage.py runserver
