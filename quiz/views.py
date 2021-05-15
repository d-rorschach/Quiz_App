from django.shortcuts import render

def index(rq):
    return render(rq, 'index.html')