#  **STICKY NOTES**
The assignment is about on Creating a sticky note website
Requirements: User should be able perform the following features
- Create
- view
- edit
- delete their sticky notes. 
- Notes should be persistent on refresh.




## Getting Started

Followed these steps to set up and complete the project on my local machine.

### Prerequisites

Before getting, I ensured that the following requirements are installed:

- Python (3.6 or higher)
- PostgreSQL
- Django


### Running this project
```shell
    git clone https://github.com/sandeepmargana/sticky-notes.git
```

```shell
    cd sticky-notes
```


```shell
    ./run.sh
```


```shell
```
### Installation and Flow

1. Clone the repository:
First I cloned the frontend part from the following [link](https://github.com/rutikwankhade/NotesWall)
```shell
   $ git clone https://github.com/rutikwankhade/NotesWall.git
```
2. Made project directory
```shell
    $ mkdir assign_backend
    $ cd assign_backend/
```
3. Setting up Virtual Enviroinment
Installed the virtual env and activated it
```shell
    $ sudo apt install python3-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
```
4. Starting the project
Started the project and tried running the server and opened that link using the browser
```shell
    $ django-admin startproject sticky
    $ python3 manage.py runserver
```
5. Migrations
```shell
   $ .. /assign_backend$ cd sticky/
   $ python3 manage.py makemigrations
   $ python3 manage.py migrate
```
6. Changing settings.py file
```shell
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "psql_notes",
        'USERNAME' : "sandeep",
        'PASSWORD' : "1234"
                    }
                }
```
7. Creating Super User
Created superuser by providing the credentials that were asked
```shell
    $ python3 manage.py createsuperuser
```
8. Static files
moved the files that are cloned on step 1 ( app.js , style.css and icons) to the folder static which is in sticky

9. collected them into static_contents
using the command below Ive collected all the changes to the new folder static_contents
```shell
    /assign_backend/sticky$ python3 manage.py collectstatic
```
10. Created templates folder
In the Templates folder I added edit.html , expand.html and index.html and made the required changes according to the requirements asked and integrated the frontend

11. After completing all the changes urls.py was like
```shell
    
from django.contrib import admin
from django.urls import path
from notes.views import home ,addNote , delNote , editNote ,expandNote , saveNote                       
urlpatterns = [
    path('home', view= home , name = "home"),
    path('add', view= addNote  , name = "add"),
    path('del', view= delNote  , name = "delNote"),
    path('edit', view= editNote  , name = "editNote"),
    path('expand', view= expandNote  , name = "expandNote"),
    path('save', view= saveNote  , name = "saveNote"),
]
```



                                               THANKYOU