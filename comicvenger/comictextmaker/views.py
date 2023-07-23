from django.shortcuts import render
import random
import pickle
import pandas as pd
from .models import MakeStory


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
    
    generated_text1 = "Rise of the Cosmic Threat\n\nIn the aftermath of the Avengers' victory against Thanos and the Infinity Stones, the world is enjoying a period of relative peace. Bruce Banner, now finding better control over his transformation into the Hulk, has been working tirelessly in his lab, searching for a way to further enhance the team's capabilities.\n\nOne day, while analyzing some alien technology brought back from a recent battle, Banner stumbles upon an ancient artifact of immense power. Unaware of its true nature, he activates the device, inadvertently opening a portal to a distant corner of the universe." 
    
    text2 = 'From this portal emerges a being of unfathomable cosmic power, calling itself \"Eldrax, the Celestial Conqueror.\"\n\nEldrax is an entity that has witnessed countless civilizations rise and fall, leaving destruction in its wake. Seeing Earth as a potential threat to its dominance, Eldrax sets its sights on the planet, determined to wipe out humanity and establish itself as the sole ruler of the cosmos.\n\nAs news of this cosmic threat reaches the Avengers, they spring into action.'

    text3 = "Tony Stark, in his Iron Man suit, leads the charge, knowing the world needs a protector now more than ever. Alongside him is Natasha Romanoff, the Black Widow, who has been working undercover and has now returned to aid her friends.\n\nCaptain America, having been discovered and thawed out of his cryogenic slumber, joins the Avengers once again, ready to defend the world he once knew. With him is his long-lost friend, Bucky Barnes, who survived the fall and has now embraced his identity as the Winter Soldier.\n\nThe team faces their most formidable opponent yet, as Eldrax proves to be nearly invincible. His powers are beyond anything they have encountered before, even surpassing that of the Infinity Stones. Despite their combined strength, the Avengers struggle to match the cosmic conqueror.\n\nAs the battle rages on, Banner realizes that the key to defeating Eldrax may lie in unlocking the true potential of the artifact he unwittingly activated. Working alongside Shuri, the brilliant Wakandan scientist, he begins to understand the artifact's purpose: it contains the knowledge and wisdom of ancient celestial beings.\n\nWith the help of the newly intelligent Hulk, Banner accesses the vast knowledge within the artifact and discovers a hidden truth - Eldrax's power is drawn from the very fabric of reality itself. To stop him, they must sever his connection to the cosmic energies.\n\nUnited in purpose, the Avengers devise a daring plan. While Iron Man, Captain America, and the Winter Soldier engage Eldrax in an all-out assault, Black Widow and Shuri work on diverting the cosmic energies away from the celestial conqueror.\n\nIn a climactic showdown, the Avengers use their combined strength and teamwork to weaken Eldrax. As Black Widow and Shuri successfully redirect the cosmic energies, the artifact resonates with the Tesseract that Howard Stark found all those years ago.\n\nIn a burst of blinding light, Eldrax is stripped of his cosmic power, reverting to a mere mortal. The Avengers seize the opportunity to imprison him within the same artifact that brought him to Earth, hoping to contain his power and prevent further threats.\n\nWith the cosmic threat neutralized, the Avengers stand victorious once again. They return the artifact to a secure location, understanding the danger it poses in the wrong hands. The world continues to rely on their heroes to protect them, knowing that the cosmos holds many secrets yet to be discovered.\n\nAnd so, the Avengers remain vigilant, always ready to face whatever challenges the universe may throw their way, knowing that together, they are Earth's mightiest defenders.\n\n(Note: This story is a fictional creation and not part of the official Marvel canon.)"
    # Select a random image from the list
    random_image = random.choice(background_images)

    return render(request, 'comictextmaker/story.html', {'random_image': random_image, 'story1': generated_text1, 'story2': text2, 'story3': text3})

def about(request):
    return render(request, 'comictextmaker/about.html') 


def generateStory(request):


    # load the model
    model = pd.read_pickle('model_file.pickle')

    # get the values from form
    prompt = request.GET['prompt']
    

    lis = []

    lis.append(prompt)

    # predict the result
    generated_text = generate_text(model, start_string="cosimic threat")
    # you can find this function in avengers.ipynb
    
    

    
    # save the data in database
    # create an object of model
    MakeStory.objects.create(

        prompt = prompt,
        story = generated_text,
    )


    return render(request, 'comictextmaker/story.html', {'story': generated_text})