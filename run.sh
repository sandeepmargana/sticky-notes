sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd sticky
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
admin
1234
python3 manage.py runserver

