from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage, Project 

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})

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
