from django.urls import path

from contact.views import  Contact,info
urlpatterns = [
    path('', Contact, name='contact'),
    path('info/', info),

]
