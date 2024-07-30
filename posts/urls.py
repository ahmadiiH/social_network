from django.urls import path
from .views import PostView , PostListView


urlpatterns = [
    path('post/', PostView.as_view(),name="post"),

    path('post/<int:post_pk>/', PostView.as_view(),name="post"),
    path('post-list/', PostListView.as_view(),name="post_list"),

]