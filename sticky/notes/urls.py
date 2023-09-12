
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
