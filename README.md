# Souls Like API

Souls like gallery is a content sharing application that is built using the django restframe work and the React front end libary which is designed around allowing users to create read update and delete content by adding posts, editing there own posts and deleting there own posts while also adding comments and likes allowing users to give feedback on posts and also save posts they find useful, this is the backend development pipepline which highlights the process of creating the Souls Like Gallery API.

## CONTENTS

- [Souls Like API](#souls-like-api)
- [Database Relationship Models](#database-relationship-models)
    - [Database Entity relationship diagram](#database-entity-relationship-diagram)
    - [Database Schema](#database-schema)
        - [Profile model](#profile-model)
        - [Game model](#game-model)
        - [Post model](#post-model)
        - [Likes model](#likes-model)
        - [Comment model](#comment-model)
- [Features](#features)
    - [Post](#post)
    - [Game](#game)
    - [Comment](#comment)
    - [Likes](#likes)
    - [Trending](#trending)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Fork project](#fork-project)
    - [Running application locally](#running-application-locally)
- [Technologies](#technologies)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Database Relationship models

### Database Entity relationship diagram

![Database ERD](docs/images/database-erd-souls-like.png)

### Database Schema 

The Database Schema for this application is using 6 created models called Profile, Posts, Likes, Trending, Game, Comments and with one imported user model every model but the Game model will have full CRUD functionality which will allow the user to create read update and delete content on the application. Each model will be referenced by its primary key the id of the actual model, these models will be able to interact with each other on the application by using Foreign Keys.

#### Profile Model

This model will be the first model which will allow users to create read update and delete there profile, this model will be accessed when a user clicks on the profile allowing them to see there posts, users will be able to update there bio on the profile page along with change there name if they wish to.

#### Game Model

This model will be accessed if the user wishes to click on the game  title and view all the posts that are linked to this title showing the game title, and the games content,  the posts linked to this game will be found inside the post model.

#### Post Model

This is the main model of the application this will allow users to have full CRUD by adding videos or images to there post. This model will also have access to the games model which will be linked by the games foreign key, users will be able to update there own post and delete there own post. To make sure the correct post is being shown the primary key will be the posts id which makes sure in the URL the correct post is being loaded. A user is also able to click on a specific post to see further content such as the amount of likes and comments.

#### Likes Model

This model uses its id as the primary key. The model will also be using the posts Foreign key to make sure once a like is left the like is being applied to the correct post. A user will be able to unlike also if they wish to choosing which posts they would like to leave likes to.

#### Comment Model

This model uses its id as the primary key to allow users to edit and delete there own comment if they wish to. This model will have full CRUD functionality, allowing a user to create a comment if logged in edit there own comment if logged in or delete there own comment if logged in. This model uses the post model as its foreign key to make sure comments are being applied to the correct post, this model will also have a content field allowing a user to provide detailed feedback.

## Features

### Post

Posts can be viewed by users that are unauthenticated and authenticated, if the user is authenticated they are able to Create, read. update and delete there posts, users will be able to search for posts by the users name, post title and the game title.

`/posts/` This is a get request to get the posts in a list view using a create view if the user is authenticated.
`/posts/:id/` This will be an update and delete view that will allow users that edit there own post and delete there own post.

### Game

Games can be viewed by users that are unauthenticated and authenticated, if the user is a superuser they are able to create, read update, and delete the games data. This will use defensive design to ensure a standard user cannot create, read, update and delete any games data ensuring only an admin superuser can do this.

`/games/` This is using a get request to show all the games in a list view which standard users can access.
`/games/create` This is a create view that will allow only the admin user to access this view otherwise return access denied message.
`/games/:id/` This will be a update and delete view that will allow the admin user to update and delete the game.


### Comment

Comments can be viewed by users that are unauthenticated and authenticated, if the user is authenticated they can create, read,update and delete there own posts. They can read other users posts but they cannot edit and delete other users posts. To make sure users cannot edit and delete other users comments this will be controlled by is owner or read only permissions.

`/comments/` This is using a get request to show all the comments in a list which standard users can view and will also be a create view that allows authenticated users to create a comment.
`/comments/:id/` This will be an update and delete view that will allow the comment author to update and delete there own comment otherwise this will be read only.

### Likes

Likes can be viewed by users that are unauthenticated and authenticated, if the user is authenticated they can create delete there own likes.

`/likes/` This is using a get request to show all the likes if the user is authenticated the create form will be visible.
`likes/:id/` This will be a delete view using a delete request if the user is the author they can remove and delete there like.

### Trending

Trending can be viewed by users that are unauthenticated and authenticated the user can view the top 10 rated posts by the posts like count.

`/trending/` This is using a get request to show all the trending posts.
`/trending/:id/` This is using a retreive api view that will allow the user to see the detailed trending post.

## Testing 

I tested this project extensively, making sure everything worked as intended this was all documented in the TestingMd file which can be viewed here [TestingMd](https://github.com/mattthughes/souls-like-api/blob/main/TESTING.md)

## Deployment

### Heroku Deployment

1. Install the requirement.txt file dependencies by typing pip -r requirements.txt
2. Add JWT tokens to the project by first installing django all auth making sure to install the correct version of all auth, add the following to the file settings.py in the  installed apps section:
```
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```

Next add the following lines of code to the settings.py file
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
}

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'souls_like_api.serializers.CurrentUserSerializer'
}
```

After this migrate the changes to the database

3. Once you have added the JWT tokens add the default pagination class and make sure your rest framework section looks like this
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```

4. Add an app route that greets the user when opening the api
5. Add a project build database by either creating an database using elephant SQL or using an existing empty database
6. Log in to Heroku or set up an account.
7. From the dashboard click create new app.
8. Name your app this will need to be unique as you cannot use an existing application name.
9. This will create the app within Heroku and will bring you to the deploy tab. From this navigate to the resources tab.
10. Add the database to the app, to do this navigate to the add ons section and search for Heroku Postgres select the package that appears and add Heroku Postgres as the database.
11. Navigate to the settings tab, within the config vars section copy this DATABASE_URL to the clipboard to use this later in your django app.
12. Within the djanjo app repository create a new file called env.py to do this type into the terminal touch env.py. Within the file create an environment variable for the DATABASE_URL pasting the address from your clipboard you copied from heroku. along with the following piece of code os.environ['DEV'] = '1'
13. Add a SECRET_KEY to the app using another another environment variable you can obtain a secret key from a random secret key generator paste this secret key into the environment variable your secret key variable should be written like this os.environ.setdefault(
    "SECRET_KEY", "Yoursecret key")
14. Add the secret key just created to your heroku config vars by adding SECRET_KEY and the key you created as the value.
15. In the settings.py file  import Path from pathlib, import os and import dj_database_url
16. insert this line if os.path.isfile("env.py"): import env into the settings.py file 
17. Remove the default secret key that django has in the settings.py file and type SECRET_KEY = os.environ.get('SECRET_KEY')
18. Next replace the default database by either commenting out the code or deleting it you can use the default database for any automated testing later, replace this database with 
```
DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
    
}
```
this will use the development database on the developer side, and on heroku the project build database will be used.
19. In the terminal migrate over any changes you have just made by typing python3 manage.py migrate you may need to make the migrations first if you do type python3 manage.py makemigrations and then the migrate command after.
20. Navigate to cloudinary in the browser and create an account or login if you already have an account.
21. From the dashboard copy the CLOUDINARY_URL and navigate over to the django app and create a new environment variable by typing os.environ[Cloudinary_URL] paste the url that you just copied after the assignment operator.
22. In Heroku add the CLOUDINARY_URL and the value you copied to the config vars.
23. Add the KEY - DISABLE_COLLECTSTATIC with the Value 1 to the config vars.
24. Navigate back to the settings.py file and add the cloudinary libaries to the installed apps the order should be cloudinary_storage then django.contrib.staticfiles and then cloudinary below this make sure you follow this order.
25. Add this section of code to the ALLOWED_HOSTS list. It should read as ALLOWED_HOSTS = [
   os.environ.get('ALLOWED_HOST'),
   'localhost',
]
26. Create a new file in the top level directory and call it Procfile
27. In the Procfile add the following code web: guincorn PROJECT_NAME.wsgi
28. Create a superuser to use on the new database migrate the changes to the new database
29. Make sure to add, commit and push changes to GitHub.
30. Add the following cors settings to the settings.py file
```
INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
 ]

 SITE_ID = 1
 MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
     ...
 ]

 if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    dev_origin = os.environ.get('CLIENT_ORIGIN_DEV')
    CORS_ALLOWED_ORIGINS.append(dev_origin)

CORS_ALLOW_CREDENTIALS = True
```
31. Navigate back to Heroku and click on the deploy tab scroll down to the  deployment method, select GitHub and confirm you would like to connect to GitHub.
32. Enter your GitHub repository Id and then select connect.
33. If you would like every change you make on your IDE to appear on the deployed app click Enable Automatic Deploy. Otherwise you can deploy this manually each time to have more control of deploys.
34. For the last step click Deploy Branch in the manual deploy section this will start to the build the app slowly once this has been built a deployed link will appear allowing to to view your deployed app.


### Running Application locally

Navigated to the GitHub Repository:

1. Click on the code drop down and click on HTTPS
2. Copy the Repository link to the clipboard
3. Open your IDE such as GitPod, CodeAnywhere or any of your choosing making sure git is also installed
4. Type git clone alongside the repository link you have just copied into the IDE terminal, the project will now be cloned for use.

### Fork Project

1. Log in or sign u to GitHub.
2. Go to the repository for this project [mattthughes/souls-like-gallery-api](https://github.com/mattthughes/souls-like-api)
3. Click the Fork button on the right corner to fork the project.

## Technologies

* Python

* The following python modules and libraries were used for this application

    * asgiref==3.8.1
    * cloudinary==1.26.0
    * cryptography==3.4.8
    * dj-database-url==0.5.0
    * dj-rest-auth==2.1.9
    * dj3-cloudinary-storage==0.0.6
    * Django==4.2
    * django-allauth==0.54.0
    * django-cloudinary-storage==0.3.0
    * django-cors-headers==3.7.0
    * django-filter==2.4.0
    * djangorestframework==3.14.0
    * djangorestframework-simplejwt==4.7.2
    * gunicorn==20.1.0
    * oauthlib==3.1.1
    * Pillow==8.2.0
    * psycopg2==2.9.9
    * PyJWT==2.1.0
    * python3-openid==3.2.0
    * pytz==2021.1
    * requests-oauthlib==1.3.0
    * sqlparse==0.4.1
    * urllib3==1.26.18

## Credits

Backend api inspired by the DRF API walkthrough project which was customised to my projects needs found [here](https://github.com/Code-Institute-Solutions/drf-api)

## Acknowledgements

* I would like to thank my mentor dick which helped me with the project, the code institute tutors were incredibly helpful with understanding errors and why they were happening
* I would like to thank my family and friends which helped test key features during development which assisted me with bug fixes