from . import views
from django.urls import path


urlpatterns = [
    path("", views.start_page, name="start-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")  # slug: checks for slug format
]
