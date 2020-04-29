from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'content': ['Телефон для связи', '+7-999-22-55-698']})
