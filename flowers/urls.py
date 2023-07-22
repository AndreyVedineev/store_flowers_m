from django.urls import path

from flowers import views
from flowers.apps import FlowersConfig
from flowers.views import index, contacts, flowers_card


app_name = FlowersConfig.name

urlpatterns = [

    path("", index, name='index'),
    path("contacts/", views.contacts, name="contacts/"),
    path("<int:pk>/flowers_card/", views.flowers_card, name="flowers_card/")


]