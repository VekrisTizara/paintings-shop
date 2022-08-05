# Paintings shop



``` sh
git clone https://github.com/VekrisTizara/paintings-shop.git
cd paintings-shop/
python -m venv venv
. ./venv/Scripts/activate
pip install -r requirements.txt
cd shop
python manage.py migrate
winpty python ./manage.py createsuperuser
python manage.py runserver
```
