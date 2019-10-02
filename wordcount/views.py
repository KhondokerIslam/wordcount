from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html'  )

def about(request):
    return render( request, 'about.html' )

def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()

    dic = {}

    for words in wordcount:
        if words in dic:
             dic[words] +=1
        else:
             dic[words] = 1
    arra =  sorted(dic.items(), key = operator.itemgetter(1), reverse = True)
    
    return render(request, 'count.html', { 'fulltext' : fulltext, 'count' : len(wordcount), 'dic' : arra } )