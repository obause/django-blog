from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomePageView.as_view(), name="start-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page")  # slug: checks for slug format
]
