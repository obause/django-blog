from datetime import date

from django.shortcuts import render

posts_content = [
    {
        "slug": "dummy-example-post",
        "image": "mountains.jpg",
        "author": "Ole Bause",
        "date": date(2022, 12, 7),
        "title": "Dummy Example Post",
        "excerpt": "Dies ist die Beschreibung zu diesem Dummy Post, um das Design zu testen.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!
            """
    },
    {
        "slug": "dummy-example-post2",
        "image": "coding.jpg",
        "author": "Ole Bause",
        "date": date(2022, 12, 6),
        "title": "Second Dummy Example Post",
        "excerpt": "Dies ist die Beschreibung zu diesem zweiten Dummy Post, um das Design zu testen.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!
            """
    },
    {
        "slug": "third-dummy-example-post",
        "image": "woods.jpg",
        "author": "Ole Bause",
        "date": date(2022, 12, 5),
        "title": "Third Dummy Example Post",
        "excerpt": "Dies ist die Beschreibung zu diesem dritten Dummy Post, um das Design zu testen.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium doloremque, mollitia voluptatem qui
            voluptatum odio quae minus cumque et autem, nihil numquam ipsam aliquam molestiae, facere veritatis
            reprehenderit pariatur! Qui!
            """
    }
]


def get_date(post):
    return post.get('date')


# Create your views here.
def start_page(request):
    sorted_posts = sorted(posts_content, key=get_date, reverse=True)
    latest_posts = sorted_posts[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all_posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
