from django.http import HttpResponse
from django.shortcuts import redirect, render
from oswaldtruz.settings import EMAIL_HOST_USER
from contact.forms import contactForm
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def Contact(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data['name']
        userEmail = form.cleaned_data['userEmail']
        sub = form.cleaned_data['sub']
        message = form.cleaned_data['message']
        data_list = '\nName :    ' + name + '\nSubject  :   ' + \
            sub + '\nMessage   :    ' + message + '\nEmail  :    ' + userEmail
        print(data_list)
        resend_Data = 'Hey ,' + \
            name+' Thanks for connecting 🥰 Your message means alot to me.If you have any queries,suggestions and anything ,feel free to  Contact me.You can contact me on my E-mail :- ' + \
            EMAIL_HOST_USER + ' as well as on contact number :-+91 9818155505\nRegards :\nOswaldtruz.in \n '
        print(resend_Data)

        send_mail("Contact Details", data_list,
                  userEmail, [EMAIL_HOST_USER], fail_silently=False)
        send_mail("Thank You For Connecting.", resend_Data,
                  EMAIL_HOST_USER, [userEmail], fail_silently=False)
        messages.success(
            request, 'Message sent')
        print("mail sent successfully")
    else:
        messages.error(
            request, 'Invalid !!!!!')

    
    
    return render(request, "Contact.html")

def info(request):
    return HttpResponse("Info page")
