from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    # 모든 Post레코드를 가져와 저장, 데이터베이스에 쿼리를 날려 원한는 레코드를 가져올 수 있다.
    posts = Post.objects.all().order_by('-pk');

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts
        }
    )