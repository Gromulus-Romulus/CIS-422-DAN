# Sends randomly-generated dog profiles to database.
#
# Author: Nathan M.
#

from DANv1.website.dogdb import add_dog, delete_dog, get_dogs, get_dog_by_ID

# import dog profiles from csv table

with open("./DAN_dog_profiles.csv") as PROFILES:
    header = PROFILES.readline()

    for line in PROFILES:

        # Split by comma and get rid of ID
        fields = line.split(',')

        [
            name, photo_id, sex, age, breed, grouping, weight, notes,
            neutered, walks, barking, trained,
            yard_req, friendly, energy,
            attention_req, good_with_pets,
            good_with_kids, shedding, size
        ] = fields

        # add dog to database
        add_dog(name, photo_id, sex, age, breed, grouping,
               weight, notes, neutered,
               walks, barking, trained,
               yard_req, friendly, energy,
               attention_req, good_with_pets,
               good_with_kids, shedding, size)