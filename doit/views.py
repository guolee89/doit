# cooding: utf-8

from django.shortcuts import render_to_response


def home(request):
    ''' blog home '''

    return render_to_response('doit/index.html')
