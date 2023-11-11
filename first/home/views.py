from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Departments,Doctors
# Create your views here.
def index(request):
    # person={
    #     'name':'John',
    #     'age':'25',
    #     'place':'calicut',
    # }
    numbers={
        'num1':[1,2,3,4,5,6,7,8,9,10],
        'fruits':['banana','apple','grapes']
    }
    return render(request, 'index.html',numbers)

def about(request):
    return render(request, 'about.html')
    
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form =BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)
    

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all   # pylint: disable=E1101
    }
    return render(request, 'doctors.html',dict_docs)
   

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept ={
        'dept':Departments.objects.all()  # pylint: disable=E1101
        }
    return render(request, 'department.html',dict_dept)