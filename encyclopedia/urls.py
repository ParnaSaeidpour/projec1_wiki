from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.Entry_Page, name="Entry_Page"),
    path("Search_Page", views.Search_Page, name="Search_Page")
]
