from django.urls import path

from flowers import views
from flowers.apps import FlowersConfig
from flowers.views import contacts, IndexListView, flowers_card, Blog_flCreateView, Blog_flListView, Blog_flDetailView, \
    Blog_flUpdateView

app_name = FlowersConfig.name


class BBlog_flUpdateView:
    pass


urlpatterns = [

    path("", IndexListView.as_view(), name='flowers_list'),
    path("contacts/", views.contacts, name="contacts/"),
    path("<int:pk>/flowers_card/", flowers_card, name="flowers_card/"),
    path("create/", Blog_flCreateView.as_view(), name="blog_fl_form/"),
    path("edit/<int:pk>/", Blog_flUpdateView.as_view(), name="update_blog_fl_form/"),
    path("list/", Blog_flListView.as_view(), name="blog_fl_list/"),
    path("/detail/<int:pk>", Blog_flDetailView.as_view(), name="blog_fl_detail/")

]


# urlpatterns = [
#
#     path("", index, name='index'),
#     path("contacts/", views.contacts, name="contacts/"),
#     path("<int:pk>/flowers_card/", views.flowers_card, name="flowers_card/")
#
#
# ]