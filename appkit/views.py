from django.shortcuts import render, redirect
from .models import Testimonials
from .forms import FeedBack

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            feedback = form.save()
            feedback.save()
            #return redirect('appkit/testimonials.html')
            form = FeedBack()
    else:
        form = FeedBack()
    tims = Testimonials.objects.all()
    return render(request, 'appkit/index.html', {'tims': tims, 'form': form})

def testimonials(request):
    tims = Testimonials.objects.all()
    return render(request, 'appkit/testimonials.html', {'tims': tims})
