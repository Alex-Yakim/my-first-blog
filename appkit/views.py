from django.shortcuts import render
from .models import Testimonials

# Create your views here.
def home_page(request):
    tims = Testimonials.objects.all()
    return render(request, 'appkit/index.html', {'tims': tims})

def testimonials(request):
    tims = Testimonials.objects.all()
    return render(request, 'appkit/testimonials.html', {'tims': tims})
