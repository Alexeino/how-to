from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name="homepage"),
    path('add_note/',add_note,name="add_note"),
    path('note_details/<slug:slug>',note_details,name="note_details"),
    path('loginPopup/',loginPopup,name="loginPopup"),
    path('search_view/',search_view,name="search_view")
]
