from django.shortcuts import render
from django.http import HttpResponse
from .models import FORM_DATA_FROM_USERS
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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


        # subject = 'Subject'
        # html_message = render_to_string('mail_template.html', {'user_name': request.POST.get('user_name'), 'user_email':request.POST.get('user_email'),'user_zipcode':request.POST.get('user_zipcode'),'user_city':request.POST.get('user_city'),
        # 'user_state':request.POST.get('user_state'),'user_address':request.POST.get('user_address'),'mobile_number':request.POST.get('mobile_number'),'whatsapp_number':request.POST.get('whatsapp_number'),
        # 'distributor':request.POST.get('distributor'),'counter_type':request.POST.get('counter_type'),'electricity_consumption':request.POST.get('electricity_consumption'),
        # 'surface_ownership':request.POST.get('surface_ownership'),'type_of_roof':request.POST.get('type_of_roof'),'user_interest':request.POST.get('user_interest')})
        # plain_message = strip_tags(html_message)
        # from_email = 'From <from@example.com>'
        # to = request.POST.get('user_email')
        # mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        
        
    return render(request,'submit.html')
