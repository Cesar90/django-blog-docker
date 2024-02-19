from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.
def index(request):
    # # print(dir(request))
    # news = News.objects.all()
    # res = '<h1>News</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div><hr>\n'
    # # return HttpResponse('Hello world')
    # return HttpResponse(res)
    # news = News.objects.order_by('-created_at')
    news = News.objects.all()
    context = {
        'news':news,
        'title':'News Index'
    }
    return render(request, template_name='news/index.html', context=context)

def test(request):
    return HttpResponse('<h1>Test testing</h1>')