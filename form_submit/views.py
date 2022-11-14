from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def form(request):
    return render(request,'index.html')

def submit(request):
    if request.POST.get('user_name'):
        post = Post()
        post.user_name = request.POST.get('user_name')
        post.user_email = request.POST.get('user_email')
        post.user_zipcode = request.POST.get('user_zipcode')
        post.user_city = request.POST.get('user_city')
        post.user_state = request.POST.get('user_state')
        post.user_address = request.POST.get('user_address')
        post.html_format = request.POST.get('html_format')
        post.save()
        
    return render(request,'submit.html')
