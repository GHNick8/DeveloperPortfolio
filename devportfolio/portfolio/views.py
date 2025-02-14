from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import ContactForm
from .models import ContactMessage, Project 

def home(request):
    return render(request, 'portfolio/home.html')

def portfolio(request):
    projects = Project.objects.all().order_by('-created_at')
    paginator = Paginator(projects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'portfolio/portfolio.html', {'page_obj': page_obj})

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            messages.success(request, "Your message has been sent successfully!") 
            form = ContactForm() 

    return render(request, 'portfolio/contact.html', {'form': form})
