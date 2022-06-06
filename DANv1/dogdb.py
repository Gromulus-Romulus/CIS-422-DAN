# includes
import mysql.connector

db = mysql.connector.connect(
host="ix-dev.cs.uoregon.edu",
user="guest",
password="guest",
port=3144,
database="dogs")

insertDog = (
    '''
    INSERT INTO DOG
    (name, photo, sex, age, breed, grouping, weight, notes, fixed, walks, barking, trained, training_time, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
)

mycursor = db.cursor(buffered=True)
def get_dogs():
    mycursor.execute("SELECT * FROM DOG")
    dogList = []
    for x in mycursor:
        # print(x)
        dogList.append(x)
    return dogList
    
def delete_dog(dogID): 
    mycursor.execute("DELETE FROM DOG WHERE ID = %s", (dogID,))
    db.commit()

def get_dog_by_ID(dogID):
    mycursor.execute("SELECT * FROM DOG WHERE ID = %s", (dogID,))
    data = mycursor.fetchall()
    if data:
        return data[0]
    else:
        return 0

def add_dog(
name, photo, sex, age, breed, grouping, weight, notes, 
fixed, walks, barking, trained, 
training_time, yard_req, friendly, 
energy, attention_req, good_with_pets,
good_with_kids, shedding, size):
    mycursor.execute(insertDog, (name, photo, sex, age, breed, grouping, weight, notes, fixed, walks, barking, trained, training_time, yard_req, friendly, energy, attention_req, good_with_pets, good_with_kids, shedding, size,))
    db.commit()


# add_dog("Juan", "photoID", "M", 10, "horse", "cool", 21, "needs beach ball", 0, 1, 0, 2, 2, 1, 1, 0, 1, 1, 1, 1, 0)
# print(get_dogs())
# delete_dog(7)
# print(get_dog_by_ID(53))
