from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(request)
    print(request.scheme)
    print(request.path)
    print(request.encoding)
    return HttpResponse('<h1>Hello World!</h1>')

""" def index_2(request):
    return HttpResponse('<h1>Hello World! index_2</h1>') """

def about(request):
    print('http://127.0.0.1:8000'+request.get_full_path())
    return HttpResponse('<a href="#"> About page! </a>')

def contacts(request):
    print(request.path)
    return HttpResponse('<h2> Contacts page </h2>')

def ggg(request):
    return HttpResponse('<h2> GGG page </h2>')

def archive(request):
    return HttpResponse('Archive page')

def archive_2(request):
    return HttpResponse('Archive page 2')

def group(request):
    group_number = request.path
    return HttpResponse('group #{group_number}')

def home_1(request):
    header = "<h1>Готовый заголовок</h1>"
    page_content = """
    <html>
    <head>
        <title>Домашняя страница</title>
    </head>
    <body>
        {}
    </body>
    </html>
    """.format(header)

    return HttpResponse(page_content)