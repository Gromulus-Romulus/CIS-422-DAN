# Script for generating random dog profiles based
# on American Kennel Club groups.
#
# Author: Nathan Malamud
# Date Created: 05.30.2022
#

import itertools
import random
import numpy

# Source: https://www.akc.org/expert-advice/lifestyle/7-akc-dog-breed-groups-explained/
groups = [
    "sporting", # Bred to capture animals
    "hound",    # Bred to sniff out prey
    "working",  # Bred to pull sleds and protect families
    "terrier",  # Bred to dig out vermin
    "non-sporting", # miscellaneous category
    "toy"   # Comfy, affectionate lap dogs
]

# 2-dimensional list of lists, ordered by AKC group
all_breeds = [
    ["labrador retriever", "german shorthaired pointer"],
    ["bloodhound"],
    ["boxer", "great dane", "rottweiler"],
    ["bull terrier", "scottish terrier", "west highland white terrier"],
    ["bulldog", "dalmatian", "poodle"],
    ["pug", "shih tzu", "chihuahua"]
]

class Dog:

    def __init__(self, name, sex, age, breed):
        self.name = name
        self.sex = sex
        self.age = age
        self.breed = breed 

        self.neutered = random.choice(("Yes", "No"))
        self.friendly = random.choice(["Very friendly", "Friendly but cautious", "Not friendly"])
        self.energy = random.choice(["High", "Medium", "Low"])
        self.attention = random.choice(["High", "Medium", "Low"])
    
    def __repr__(self):
        return f"{self.name}, {self.sex}: {self.age}-year old {self.breed}"

    def __str__(self):
        return f"""{repr(self)}
            Neutered: {self.neutered}
            {self.friendly}
            {self.energy} energy needs
            {self.attention} attention needs
        """

# Make some dogs
m_names = ["Max", "Ralph", "Rex", "Rico", "Cookie", "Brett", "Tank", "Riley", "Tucker", "Jackie", "Robbie", "Alex"]
f_names = ["Max", "Maxxie", "Oreo", "Cookie", "Ona", "Tank", "Riley", "Jackie", "Alex"]

num_dogs = 15

dog_sexes = random.choices(["M", "F"], k=num_dogs)

name_by_sex = lambda s : random.choice(m_names) if s == "M" else random.choice(f_names)
dog_names = [name_by_sex(s) for s in dog_sexes]

dog_groupIDs = numpy.random.randint(0, len(groups), size=num_dogs)

breed_by_group = lambda g : random.choice(all_breeds[g])
dog_breeds = [breed_by_group(g) for g in dog_groupIDs]

# no puppies, sorry
dog_ages = numpy.random.randint(3, 8, size=num_dogs)

dog_list = []

for i in range(num_dogs):
    name = dog_names[i]
    sex = dog_sexes[i]
    age = dog_ages[i]
    breed = dog_breeds[i]
    
    new_dog = Dog(name, sex, age, breed)
    dog_list.append(new_dog)

# Print out the data
for dog in dog_list:
    print(dog)
