# ID, name, age, weight, sex, breed, notes, neutered, walks, barking, trained, training_time, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size, photo


# this class is only used to display an individual dog's profile
# it's structured like this to make it easier to manage changes to the database structure 
class Dog:
    def __init__(self, ID, name, age, weight, sex, breed, notes, neuspay, walks, barking, trained, training_time, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size, photo, group):
        self.id = ID
        # maybe just generate size from weight using a range
        self.name = name
        if(sex == 'F'):
            self.sex = "Female"
        elif(sex == 'M'):
            self.sex = "Male"
        else:
            self.sex = sex
        
        if size == 1:
            self.size = "Small"
        elif size == 2:
            self.size = "Medium"
        elif size == 3:
            self.size = "Large"
        else:
            self.size = ""
        self.age = age
        self.breed = breed
        self.weight = weight
        self.bio = notes
        self.neuspay = neuspay


# def render_dog(dbTuple)
# TODO two different types of dog objects? or one type that always has redundancies?