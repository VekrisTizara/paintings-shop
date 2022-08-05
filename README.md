# Paintings shop


run the following commands to set up the project locally to development

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

After, the server will start at http://127.0.0.1:8000/
