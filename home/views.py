from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    peoples = [
        {'name':'Viren Mali', 'age':'42'},
        {'name':'Viren', 'age':'12'},
        {'name':'Viren Mi', 'age':'26'},
        {'name':'Viren li', 'age':'2'},
        {'name':'Viren i', 'age':'23'}
    ]

    return render(request, "index.html", context= {'page':'Home','peoples' : peoples})
 
def about(request):
    peoples = [
        {'name':'Viren Mali', 'age':'42'},
        {'name':'Viren', 'age':'12'},
        {'name':'Viren Mi', 'age':'26'},
        {'name':'Viren li', 'age':'2'},
        {'name':'Viren i', 'age':'23'}
    ]
    return render(request, "home/about.html", context={'page':'About','peoples': peoples})

def contact(request):
    
    context = {'page' : 'contact'}
    return render(request, "home/contact.html", context)