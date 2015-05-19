from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from collections import defaultdict
from collections import OrderedDict
from .models import Article



def Index(req):
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
    context = {'title':'sfsdxxxxf', 'nbar':'works'}
    return render_to_response('works.html', context)

def About(req):
    context = {'title':'sfsdxxxxf', 'nbar':'about'}
    return render_to_response('about.html', context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

