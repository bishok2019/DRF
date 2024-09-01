from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):

    context = {
        'posts' : Post.objects.all()
    }
    return render (request, 'myapp/home.html',context)

def about(request):
    return render (request, 'myapp/about.html')

# def about(request):
#     return HttpResponse('<h1>Blog About Page</h1>')

# def contact(request):
#     return HttpResponse('<h1>Blog Contact Page</h1>')
def contact(request):
    return render (request, 'myapp/contact.html')