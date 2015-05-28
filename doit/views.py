# cooding: utf-8

from django.shortcuts import render_to_response
import logging

from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from web.models import Article

logger = logging.getLogger(__name__)


def home(request):
    ''' blog home '''

    return render_to_response('doit/base.html')

class IndexView(ListView):
    
    context_object_name = 'article_list'
    template_name = 'doit/index_view.html'

    def get_queryset(self):
	
	return Article.objects.all()

class ArticleDetailView(DetailView):

    context_object_name = 'article_detail'
    template_name = 'doit/article_detail_view.html'

    queryset = Article.objects.all()

    def get_object(self):
	object = super(ArticleDetailView, self).get_object()
	return object
