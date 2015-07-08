from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from collections import defaultdict
from collections import OrderedDict
from .models import Article, Category, Tag, Config

def Index(req):

    static_page = req.get_full_path().split('/')[-1]
    suffix = static_page.split('.')[-1]
    if suffix == 'html' or suffix == 'htm':
        return render_to_response(static_page)

    articles = Article.objects.order_by('-create_date')
    paginator = Paginator(articles, 6)

    page_idx = req.GET.get('page')
    try:
        articles = paginator.page(page_idx)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'articles':articles, 'nbar':'index'}
    return render_to_response('index.html', context)

def Archives(req):
    articles = Article.objects.order_by('-create_date')
 
    years = list()
    articles_by_year = defaultdict(list)
    year = articles[0].create_date.year
    years.append(year)
    for article in articles:
        cur_year = article.create_date.year
        articles_by_year[cur_year].append(article)
        if year != cur_year:
            year = cur_year 
            years.append(year)

    archives = OrderedDict()
    for year in years:
        archives[year] = articles_by_year[year]
   
    context = {'archives':archives, 'nbar':'archives'}
    return render_to_response('archives.html', context)

def Works(req):
    works = Config.objects.get(title='works')
    context = {'works':works, 'nbar':'works'}
    return render_to_response('works.html', context)

def About(req):
    about = Config.objects.get(title='about')
    context = {'about':about, 'nbar':'about'}
    return render_to_response('about.html', context)

def Book(req):
    book = Config.objects.get(title='book')
    context = {'book':book, 'nbar':'book'}
    return render_to_response('book.html', context)

def Activity(req):
    activity = Config.objects.get(title='activity')
    context = {'activity':activity, 'nbar':'activity'}
    return render_to_response('activity.html', context)

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'

def CategoryHome(req, slug):
    cur_category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=cur_category).order_by('-create_date')
    paginator = Paginator(articles, 6)
    page_idx = req.GET.get('page')
    try:
        articles = paginator.page(page_idx)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'articles':articles, 'nbar':'categories_home'}
    return render_to_response('categories_home.html', context)

def TagHome(req, slug):
    cur_tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(tag=cur_tag).order_by('-create_date')
    paginator = Paginator(articles, 6)
    page_idx = req.GET.get('page')
    try:
        articles = paginator.page(page_idx)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'articles':articles, 'nbar':'tags_home'}
    return render_to_response('tags_home.html', context)

