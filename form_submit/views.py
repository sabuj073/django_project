from django.shortcuts import render
from django.http import HttpResponse
from .models import FORM_DATA_FROM_USERS
from django.core.mail import send_mail


# Create your views here.
def form(request):
    return render(request,'index.html')

def submit(request):
    if request.POST.get('user_name'):
        post = FORM_DATA_FROM_USERS()
        post.user_name = request.POST.get('user_name')
        post.user_email = request.POST.get('user_email')
        post.user_zipcode = request.POST.get('user_zipcode')
        post.user_city = request.POST.get('user_city')
        post.user_state = request.POST.get('user_state')
        post.user_address = request.POST.get('user_address')
        post.mobile_number = request.POST.get('mobile_number')
        post.whatsapp_number = request.POST.get('whatsapp_number')
        post.distributor = request.POST.get('distributor')
        post.counter_type = request.POST.get('counter_type')
        post.electricity_consumption = request.POST.get('electricity_consumption')
        post.surface_ownership = request.POST.get('surface_ownership')
        post.type_of_roof = request.POST.get('type_of_roof')
        post.user_interest = request.POST.get('user_interest')
        post.save()

        
        
    return render(request,'submit.html')
