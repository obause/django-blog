from django.shortcuts import render, get_object_or_404

from .models import Post


def get_date(post):
    return post.get('date')


# Create your views here.
def start_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all_posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post = next(post for post in posts_content if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post,
        "tags": post.tags.all()
    })
