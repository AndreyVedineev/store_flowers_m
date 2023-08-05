from django.urls import path

from flowers import views
from flowers.apps import FlowersConfig
from flowers.views import contacts, IndexListView, Blog_flCreateView, Blog_flListView, Blog_flDetailView, \
    Blog_flUpdateView, Blod_flDeleteView, toggle_activity, FlowersCreateView, FlowersUpdateView

app_name = FlowersConfig.name


class BBlog_flUpdateView:
    pass


urlpatterns = [

    path("", IndexListView.as_view(), name='flowers_list'),
    path("create/flowers/", FlowersCreateView.as_view(), name='flowers_create/'),
    path("update/<int:pk>/flowers/", FlowersUpdateView.as_view(), name='flowers_update/'),


    # path("<int:pk>/flowers_card/", flowers_card, name="flowers_card/"),



    path("create/", Blog_flCreateView.as_view(), name="blog_fl_form/"),
    path("edit/<int:pk>/", Blog_flUpdateView.as_view(), name="update_blog_fl_form/"),
    path("list/", Blog_flListView.as_view(), name="blog_fl_list/"),
    path("detail/<int:pk>", Blog_flDetailView.as_view(), name="blog_fl_detail/"),
    path("delete/<int:pk>/", Blod_flDeleteView.as_view(), name="blog_fl_confirm_delete/"),
    path("activity/<int:pk>", toggle_activity, name="toggle_activity/"),

    path("contacts/", views.contacts, name="contacts/"),

]


# urlpatterns = [
#
#     path("", index, name='index'),
#     path("contacts/", views.contacts, name="contacts/"),
#     path("<int:pk>/flowers_card/", views.flowers_card, name="flowers_card/")
#
#
# ]