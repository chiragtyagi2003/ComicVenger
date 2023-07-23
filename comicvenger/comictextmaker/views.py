from django.shortcuts import render
import random

# Create your views here.

# index view
def index(request):
    return render(request, 'comictextmaker/index.html')


def home(request):
    return render(request, 'comictextmaker/home.html')

def story(request):
    # List of background images
    background_images = [
        'comictextmaker/captain_america.jpg',
        'comictextmaker/evil.jpg',
        'comictextmaker/iron_man.jpg',
        'comictextmaker/meet.jpg',
        'comictextmaker/office.jpg',
        'comictextmaker/plane.jpg',
        'comictextmaker/spaceship.jpg',
        'comictextmaker/spider_man.jpg',
        'comictextmaker/stark.jpg',
        'comictextmaker/thanos.jpg',
        # Add more background images as needed
    ]

    # Select a random image from the list
    random_image = random.choice(background_images)

    return render(request, 'comictextmaker/story.html', {'random_image': random_image})

def about(request):
    return render(request, 'comictextmaker/about.html') 


def generateStory(request):
    