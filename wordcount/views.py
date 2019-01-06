from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(request):
    return render(request, 'home.html',)

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordcountdict = {}

    for word in wordlist:
        if word in wordcountdict:
            #icerement
            wordcountdict[word] += 1
        else:
            #add to the dict
            wordcountdict[word] = 1


    sortedwords = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
