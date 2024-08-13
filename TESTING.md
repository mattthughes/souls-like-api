# Testing

Welcome to testing results of The Advanced Frontend Application known as Souls Like Gallery in this document you will find all the testing resuts such as solved bugs, how they were fixed any known bugs, manual and automated testing as well and how they were tested making sure each element worked as intended.

## CONTENTS
- [Testing](#testing)
- [Python Validation](#python-validation)
    - [Posts](#posts)
    - [Games](#games)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Trending](#trending)
- [Solved Bugs](#solved-bugs)
- [Known Bugs](#known-bugs)
- [Manual Testing](#manual-testing)
    - [Aims](#aims)
    - [Testing Steps](#testing-steps)
    - [Testing Results](#testing-results)
- [Automated Testing](#automated-testing)
    - [Aims](#automated-testing-aims)
    - [Testing Logic](#testing-logic)
    - [Testing Results](#automated-testing-results)

### Python Validation

#### Posts

`Model`

![Post Model](docs/images/post-view-validation.png)

`Serializer`

![Post Serializer](docs/images/post-serializer-validation.png)

`View`

![Post View](docs/images/post-view-validation.png)

`URL`

![Post URL](docs/images/post-urls-validator.png)

`Tests`

![Post Tests](docs/images/post-tests-validation.png)

#### Games

`Model`

![Game Model](docs/images/game-model-validation.png)

`Serializer`

![Game Serializer](docs/images/game-serializer-validation.png)

`View`

![Game View](docs/images/game-views-validation.png)

`URL`

![Game URL](docs/images/game-urls-validation.png)

`Tests`

![Game Tests](docs/images/game-tests-validation.png)

#### Comments

`Model`

![Comments Model](docs/images/comments-model-validation.png)

`Serializer`

![Comments Serializer](docs/images/comment-serializer-validation.png)

`View`

![Comments Views](docs/images/comment-view-validation.png)

`URL`

![Comments URL](docs/images/comments-url-validation.png)

`Tests`

![Comments Tests](docs/images/comments-tests-validation.png)



#### Likes

`Model`

![Like Model](docs/images/like-model-validation.png)

`Serializer`

![Lke Serializer](docs/images/like-serializer-validation.png)

`View`

![Like View](docs/images/like-views-validation.png)

`URL`

![Like URL](docs/images/like-ulrs-validation.png)

`Tests`

![Like Tests](docs/images/like-tests-validation.png)

#### Trending

`View`

![Trending view](docs/images/trending-view-validation.png)

`URL`

![Trending URL](docs/images/trending-urls-validation.png)

`Tests`

![Trending Tests](docs/images/trending-tests-validation.png)


### Solved Bugs

* Adjusted profile views was running into errors regarding the post model which I haven't created yet adjusted profile view to generic profile view to remove mention of the post model, the view will be changed at a later date once the post model is created.
* Fixed CRSF Forbidden error when trying to log into api added CRSF trusted origins to settings.py and added development site name to the new CRSF variable which fixed this issue.
* Fixed Game authentication error orginally any authenticated user could create a game or delete there own game which was not the intended purpose. Only the admin user is able to do this. To fix this I adjusted the permissions from authenticated read only to isAdmin, which was checking if the user logged in has admin priveliges, if they do the create view will work otherwise a permission denied message will appear.
* While trying to use the file field for my post model I was only able to upload images uploading any other file type would crash the server, could not find an issue for this when changing the field back to an image field I ran into many errors to fix this I flushed the database and migrated all the models again which fixed these errors.
* Fixed file filed issues by importing VideoMediaCloudinaryStorage from cloudinary and then setting the video field to have a storage argument with the VideoMediaCloudinaryStorage as its argument which fixed this issue.
* Fixed search bug initally while trying to search for a game an I contains error would appear, in order to fix this I targeted the game title along with the game model which allowed me to search for a post by the game associated with this post which fixed this issue.
* Fixed JWT refresh token error initally when trying to login the page would refresh but not log the user in, to fix this I specified if the user was the dev in the env.py file which fixed this issue.
* Fixed bad 400 error on heroku, to fix this I turned debug to true and then saw the allowed hosts was using the http url rather than the heroku url, changing this in the allowed hosts fixed this issue.
* Fixed Game detail view originally a user that was not signed in could access the game detail game id. This error was found while creating the automated game detail tests, in order to fix this I changed the permissions to is.Admin which allowed only an admin user to access this information fixing this error.
* Fixed post view tests orginally I was recieving an error stating the game id cannot be null, to fix this I created a game within the test and assigned it to a variable called test game, after this I created the post model and set the game field to the test game fixing this issue.
* Fixed a comment serializer issue this was trying to access the comment likes field which no longer existed removing this removed the server 500 error
* Fixed post game issue, orginally the user on the front end was only able to target the id of the game and not the actual content of the game. Which caused issues when creating posts and searching for posts under the games title. Which was not possible. To fix this I added the game field to the post serializer with a serializer slug field, setting the slug field to the title field on the games model. After this I used the games model as the query set resulting in the game title being returned rather than the id fixing this issue.
* Fixed errors in front end by adding default pagination and the page results fixing these issues.


### Known Bugs

### Manual Testing


#### Aims

* The aim of testing is to make sure all elements work as intended without any server errors

* This will be done by checking if list and detail view, while also checking if users can create read update and delete there data but cannot delete others.


### Testing Steps 

* I will test that each element works by accessing all set up urls to ensure each element works as intended.

* I will make sure only authenticated users can create, read, update and delete there data whereas updating and deleting other users data is hidden and only the owner can access this data.


`Route`

**Element**|**Expected Outcome**|**Testing Performed**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Route view|Load Welcome message|Launched API|Loaded Welcome message|Pass


### Automated Testing

#### Automated Testing Aims

* To make sure all views work as intended.
* To make sure there are not any errors during testing.
* To make sure users are only able to view data they own or have privelliges for 

#### Testing Logic

`Post Testing`

![Post Testing](docs/images/post-tests-logic.png)

`Game Testing`

![Game Testing Part 1](docs/images/game-test-part-1-logic.png)

![Game Testing Part 2](docs/images/game-test-part-2-logic.png)

`Comment Testing`

![Comment Testing Part 1](docs/images/comment-tests-part-1-logic.png)

![Comment Testing Part 2](docs/images/comment-tests-part-2-logic.png)

`Likes Testing`

![Likes Testing Part 1](docs/images/likes-tests-logic-part-1.png)

![Likes Testing Part 2](docs/images/likes-tests-logic-part-2.png)

`Trending Testing`

![Trending Testing Part 1](docs/images/trending-tests-part-1-logic.png)

![Trending Testing Part 2](docs/images/trending-tests-part-2-logic.png)


#### Testing Results

![Automated Testing Results](docs/images/test-results.png)