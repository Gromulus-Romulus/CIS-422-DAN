# ID, name, age, weight, sex, breed, notes, neutered, walks, barking, trained, training_time, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size, photo
'''
This class creates the dog profile class.
'''

class Dog:
    ''' This class is only used to display an individual dog's profile.
     It's structured like this to make it easier to manage changes to the database structure.
    '''
    def __init__(self, ID, name, photo, sex, age, breed, grouping, weight, notes, fixed, walks, barking, trained, training_time, yard_req, friendly, energy, attention_req, good_with_pets, good_with_kids, shedding, size):
        ''' Initializes all the attributes of a dog'''
        self.id = ID

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
        self.group = grouping
        self.weight = weight
        self.bio = notes
        self.neuspay = fixed
        self.walks = walks
        self.bark = barking
        self.trained = trained
        self.yard = yard_req
        self.friendly = friendly
        self.energy = energy
        self.kids = good_with_kids
        self.pets = good_with_pets
        self.shedding = shedding
        self.img = photo
        self.attention = attention_req


