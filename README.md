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
7. Run Celery (in a different terminal window)
    ```
    $ celery -A cornershopmeals worker -l info
    ``` 
   
8. Go to `localhost:8000/signup` to create a food admin employee account that will be the food admin, by checking `is_staff` option and make sure to choose good `username` and `password` otherwise Signup will not occur.
    You can also create a superuser.
    ```
    $ python manage.py createsuperuser
    ```

9. Go to `localhost:8000/login` to create some employee accounts and use the app.

10. Slack notifications are sent on a channel. Please configure your slack `WEBHOOK_URL` in [`corenershopmeals/env.ini`](https://github.com/jubins/Cornershop-Meals/blob/master/cornershopmeals/env.ini#L12) to test slack notifications.

### Tests
All the test cases are located in
- [Menu Tests](https://github.com/jubins/Cornershop-Meals/blob/master/cornershopmeals/menus/tests.py)
- [Employee Tests](https://github.com/jubins/Cornershop-Meals/blob/master/cornershopmeals/employees/tests.py)

### Contact
- Jubin Soni
- jubinsoni27@gmail.com

### Demo
This project is hosted on Heroku: feel free to create accounts `https://cornershop-meals-app.herokuapp.com/signup/` and test the app.

Login page
![](https://github.com/jubins/Cornershop-Meals/blob/master/img/login_page.png)

Open menu page
![](https://github.com/jubins/Cornershop-Meals/blob/master/img/open_menu_page.png)

Admin can view all menus
![](https://github.com/jubins/Cornershop-Meals/blob/master/img/admin_can_view_all_menus.png)

Admin can view all employee selections
![](https://github.com/jubins/Cornershop-Meals/blob/master/img/admin_can_view_all_selections.png)

Employee can choose options
![](https://github.com/jubins/Cornershop-Meals/blob/master/img/employee_option_selection.png)

Slack notifications using Celery
![](https://github.com/jubins/Cornershop-Meals/blob/master/img/slack_notifications.png)

