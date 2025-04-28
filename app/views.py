from django.shortcuts import render
import json
from django.http import Http404

# Create your views here.


file = open(r'D:\DJANGOA1\Car_rental\templates\fake_car_rental_data (1).json','r')
json_data = file.read()
cars = json.loads(json_data)

for car in cars:
    car['id'] = int(car['id'])


def home(request):
    return render(request,'home.html',{'cars':cars})

 
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')


def car_detail(request, car_id):
    # Find the car by its ID
    car = next((car for car in cars if car['id'] == car_id), None)
    if not car:
        raise Http404("Car not found")
    return render(request, 'car_detail.html', {'car': car})