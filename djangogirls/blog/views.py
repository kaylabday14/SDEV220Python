# blogs folder

from django.shortcuts import render
from datetime import datetime, timezone, timedelta
from .models import Post

# Create your views here.

def post_list(request):
    est_offset = timezone(timedelta(hours=-5))
    time_now = datetime.now(est_offset)
    posts = Post.objects.filter(published_date__lte=time_now).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})