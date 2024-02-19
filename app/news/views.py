from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

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
        'title':'News Index',
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news':news, 'category': category})