# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Desmond', 'tabby', 'Cutest and best personality.', 8),
    Cat('Donut', 'muted tortoiseshell', 'Looks like a turtle.', 3),
    Cat('Monkey', 'black tabby', 'Happy fluff ball.', 8),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


