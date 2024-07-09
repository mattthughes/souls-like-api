# Souls Like API

Souls like gallery is a content sharing application that is built using the django restframe work and the React front end libary which is designed around allowing users to create read update and delete content by adding posts, editing there own posts and deleting there own posts while also adding comments and likes allowing users to give feedback on posts and also save posts they find useful, this is the backend development pipepline which highlights the process of creating the Souls Like Gallery API.

## CONTENTS



## Database Relationship models

### Database Schema 

The Database Schema for this application is using 6 created models called Profile, Posts, Likes, Trending, Game, Comments and with one imported user model every model but the Game model will have full CRUD functionality which will allow the user to create read update and delete content on the application. Each model will be referenced by its primary key the id of the actual model, these models will be able to interact with each other on the application by using Foreign Keys.

### Profile Model

This model will be the first model which will allow users to create read update and delete there profile, this model will be accessed when a user clicks on the profile allowing them to see there posts, users will be able to update there bio on the profile page along with change there name if they wish to.

### Game Model

This model will be accessed if the user wishes to click on the game  title and view all the posts that are linked to this title showing the game title, and the games content,  the posts linked to this game will be found inside the post model.

### Post Model

This is the main model of the application this will allow users to have full CRUD by adding videos or images to there post. This model will also have access to the games model which will be linked by the games foreign key, users will be able to update there own post and delete there own post. To make sure the correct post is being shown the primary key will be the posts id which makes sure in the URL the correct post is being loaded. A user is also able to click on a specific post to see further content such as the amount of likes and comments.

### Likes Model

This model uses its id as the primary key. The model will also be using the posts Foreign key to make sure once a like is left the like is being applied to the correct post. A user will be able to unlike also if they wish to choosing which posts they would like to leave likes to.

### Comment Model

This model uses its id as the primary key to allow users to edit and delete there own comment if they wish to. This model will have full CRUD functionality, allowing a user to create a comment if logged in edit there own comment if logged in or delete there own comment if logged in. This model uses the post model as its foreign key to make sure comments are being applied to the correct post, this model will also have a content field allowing a user to provide detailed feedback.


## Testing 

### Solved Bugs

* Adjusted profile views was running into errors regarding the post model which I haven't created yet adjusted profile view to generic profile view to remove mention of the post model, the view will be changed at a later date once the post model is created.
* Fixed CRSF Forbidden error when trying to log into api added CRSF trusted origins to settings.py and added development site name to the new CRSF variable which fixed this issue.
* Fixed Game authentication error orginally any authenticated user could create a game or delete there own game which was not the intended purpose. Only the admin user is able to do this. To fix this I adjusted the permissions from authenticated read only to isAdmin, which was checking if the user logged in has admin priveliges, if they do the create view will work otherwise a permission denied message will appear.
* While trying to use the file field for my post model I was only able to upload images uploading any other file type would crash the server, could not find an issue for this when changing the field back to an image field I ran into many errors to fix this I flushed the database and migrated all the models again which fixed these errors.
* Fixed file filed issues by importing VideoMediaCloudinaryStorage from cloudinary and then setting the video field to have a storage argument with the VideoMediaCloudinaryStorage as its argument which fixed this issue.
* Fixed search bug initally while trying to search for a game an I contains error would appear, in order to fix this I targeted the game title along with the game model which allowed me to search for a post by the game associated with this post which fixed this issue.
* Fixed JWT refresh token error initally when trying to login the page would refresh but not log the user in, to fix this I specified if the user was the dev in the env.py file which fixed this issue.
* Fixed bad 400 error on heroku, to fix this I turned debug to true and then saw the allowed hosts was using the http url rather than the heroku url, changing this in the allowed hosts fixed this issue.