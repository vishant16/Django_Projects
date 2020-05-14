# User Activity

## Implementation steps (using Django Framework)
    1. Custom management command
    2. Implementation of an API.
    3. Endpoints
    4. version requirement


### 1. Custom management command
  #### 1. It is implemented to insert dummy data into database

  #### 2. Command name given
  python manage.py usercommand

  #### 3. How it works
  1. There is a json file named as "dummy.json" there we need to insert few details like id,real_name,tz,start_time and end_time.

  2. After reading data from dummy.json file it inserts data into database
    2.1 if id is unique it will create fresh new user activity details.
    2.2 if id is already present in database, it will add only start_time and end_time to existing user mentioned in the id.


### 2. Implementation of an API
There is two models- User and Activity
User Model has attributes id, real_name and tz
Activity Model has attributes user(ForeignKey to User Model),start_time and end_time

There is use of serializers from rest_framework for data representation and it also help us to convert model instance and queryets into python normal datatypes that can be rendered to JSon and XML.

Use of ListCreateAPIView which is used for reading endpoints to represent model instances

### 3. Endpoints
  http://useractivity.pythonanywhere.com/api/user_activity/   - which displays user activities

### 4. Version Requirements
  djang0==3.0.4
  rest_framework = 3.11.0
