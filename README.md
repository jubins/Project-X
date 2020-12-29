# Cornershop-Meals
Cornershop meals is a meal management service that provides a very convenient way of meal reservation to Cornershop employees. Allowing admin (Nora) to send slack messages and view all the employee choices.
Go to the [menu](https://cornershop-meals-app.herokuapp.com/menu/) page to see what's in today's menu and use the app!

### Setup
This app is deployed on Heroku https://cornershop-meals-app.herokuapp.com.
Please follow below steps if you would like to setup the project locally.

1. Clone this repository   
    ```
    $ git clone https://github.com/jubins/Cornershop-Meals.git
    ```
2. Create a virtual env with Python 3
    ```
    $ virtualenv myprojectenv
    $ virtualenv source myprojectenv/bin/activate
    ```
3. Install dependences
    ```
    $ pip install -r requirements.txt
    ```
4. I am using Postgres database for storing the data, Redis as message broker, Celery for asynchronous slack messaging and Slack webhook. Configure these environment variables in [`corenershopmeals/env.ini`](https://github.com/jubins/Cornershop-Meals/blob/master/cornershopmeals/env.ini).
5. Apply Django migrations
    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```
6. Start Django server
    ```
    $ python manage.py runserver
    ```
7. Run Celery
    ```
    $ celery -A cornershopmeals worker -l info
    ``` 
8. Create a superuser, that will be the food admin
    ```
    $ python manage.py createsuperuser
    ```
9. Go to `localhost:8000/login` to create some employee accounts and use the app.

10. Slack notifications are sent on a channel. Please configure your slack `WEBHOOK_URL` in [`corenershopmeals/env.ini`](https://github.com/jubins/Cornershop-Meals/blob/master/cornershopmeals/env.ini#L12).

### Tests


### Contact
- Jubin Soni
- jubinsoni27@gmail.com
