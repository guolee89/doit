# -*- coding:utf-8

from django.db.models import Model, CharField, DateField, DateTimeField, TextField

# Create your models here.

class Article(Model):
    ''' 文章 '''

    title = CharField(max_length=15)

    content = TextField()

    created_at = DateTimeField(auto_now_add=True, editable=True)

    updated_at = DateTimeField(auto_now=True)




