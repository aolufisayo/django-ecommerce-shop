# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/aolufisayo/django-ecommerce-shop.git
    $ cd django-ecommerce-shop
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver