from django.shortcuts import render, redirect
from .models import Article
import datetime

# Create your views here.

def new(request):
    if request.method == 'POST':
        print(request.POST)
        # orm 이 쓰이는 부분.
        # title은 포스트 요청의 name을 작성해주고, 
        # content 네임의 정보를 contnet로 만들어줘라
        # create의 작업. 

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            date =  datetime.datetime.today().replace(microsecond=0)
        )
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    length = len(articles)

    hobby_length = len(articles.filter(category = 'hobby'))
    food_length = len(articles.filter(category = 'food'))
    programming_length = len(articles.filter(category = 'programming'))

    return render(request, 'list.html', {
        'articles': articles, 
        'length': length, 
        'hobby': 'hobby', 
        'food': 'food', 
        'programming': 'programming', 
        'hobby_length': hobby_length,
        'food_length': food_length,
        'programming_length': programming_length,
        })

def category(request, article_category):
    articles = Article.objects.all().filter(category = article_category)
    length = len(articles)

    all_articles=Article.objects.all()
    hobby_length = len(all_articles.filter(category = 'hobby'))
    food_length = len(all_articles.filter(category = 'food'))
    programming_length = len(all_articles.filter(category = 'programming'))

    return render(request, 'category.html', {
        'articles': articles, 
        'length': length, 
        'hobby': 'hobby', 
        'food': 'food', 
        'programming': 'programming',
        'article_category': article_category,
        
        'hobby_length': hobby_length,
        'food_length': food_length,
        'programming_length': programming_length,
        })


def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    print(article)
    return render(request, 'detail.html', {'article': article})