# Paintings shop


The project had been made with Django and Bootstrap, and has registration, log in and log out forms. The main page welcomes registered users by their name. 

Administrator can add items to the shop using Django administration page. There are description fields, such as name, style, price, image, etc. Each product has its page, where you can read all the information about it and add it to basket.

At checkout the program checks if items from the basket weren't already ordered, and if they were, the site shows information about it and delete those items from basket. This check exists, because assumed, that the items are unique. Users can delete items from basket and check the total cost. 

After a successful ordering, all bought items become invisible for other users and information about them is deleted from gallery page (but not from the base). 


# Running
Run the following commands to set up the project locally for development:

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
The database is sqlite, stored at /shop/db.sqlite3
