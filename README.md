# LittleLemon Project Information

## MySQL Configuration
MySQL relevant information is shown below.
If you need to test on your machine, please change it to the one with sufficient permission.
By default, using root user with empty password is not allowed to connect to MySQL server without super user privilege. 
Also it is needed to create the corresponding database beforehand or it will report error.
```
username: 'django'  
password: '' 
database name: 'LittleLemon'

```
## Project Setup
To start the virtual environment, please type the following command:
```
# in the root directory
pip3 install pipenv # pipenv installation 
pipenv install      # install local environment 
pipenv shell        # start virtual environment

# move to LittleLemon folder 
python manage.py makemigrations 
python manage.py migrate
```

## API Endpoint
The table shows the relevant api endpoint you can test.  
|endpoint| url | method | content | permission |
|------| -----| ------|------| -----|
|home| localhost:8000/restaurant| GET | show website page | anon |
|menuitem list| localhost:8000/restaurant/menu | GET, POST | show or add menu item | anon |
|single menuitem| localhost:8000/restaurant/menu/{menu_id} | GET, PUT, DELETE | edit a specific menu item given id | anon |
|user | localhost:8000/auth/users/ | POST | create new user using name and password | anon |  
|booking | localhost:8000/restaurant/booking/table | GET, POST | show or add booking information | authenticated |


## Test Files
The test files is written in Restaurant app and you can run with the command below: 
```
python manage.py test 
```
If the database user doesn't have sufficient permission, it might report test failure.