from  home import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.department,name='department'),
    
]
