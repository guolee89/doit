# coding:utf-8
import xadmin
from web.models import Article
from web.markup import restructuredtext


# Register your models here.
class ArticleAdmin(object):
    search_fields = ('title')
    fields = ('title', 'content', )
    list_display = ('title', 'created_at', 'updated_at' )
    list_display_links = ('title')
    
    ordering = ('-created_at', '-updated_at')
    list_per_page = 15
    save_on_top = True

xadmin.site.register(Article, ArticleAdmin)

