from datetime import date

from django.shortcuts import render

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'authors': 'Mea',
        'date': date(2021, 8, 5),
        'title': 'Mountain Hiking',
        'excerpt': "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        'content': """ 
            {% lorem 4 b random %}
            {% lorem 4 b random %}
            {% lorem 4 b random %}
        """
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.png',
        'authors': 'Mea',
        'date': date(2023, 11, 21),
        'title': 'Programming Is Great!',
        'excerpt': "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        'content': """ 
            {% lorem 4 b random %}
            {% lorem 4 b random %}
            {% lorem 4 b random %}
        """  
    },
    {
        'slug': 'into-the-woods',
        'image': 'woods.jpg',
        'authors': 'Mea',
        'date': date(2024, 3, 5),
        'title': 'Nature At Its Best',
        'excerpt': "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        'content': """ 
            {% lorem 4 b random %}
            {% lorem 4 b random %}
            {% lorem 4 b random %}
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
       'post': identified_post 
    })