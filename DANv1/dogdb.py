# includes
import mysql.connector

db = mysql.connector.connect(
host="ix-dev.cs.uoregon.edu",
user="guest",
password="guest",
port=3144,
database="dogs")

insertDog = (
    "INSERT INTO DOG"
    "(name, sex, age, breed, weight, notes, fixed, walks, barking, trained, training_time, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size, group)"
    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)

mycursor = db.cursor(buffered=True)
def get_dogs():
    mycursor.execute("SELECT * FROM DOG")
    dogList = []
    for x in mycursor:
        print(x)
        dogList.append(x)
    return dogList
    
def delete_dog(dogID):
    mycursor.execute("DELETE FROM DOG WHERE ID = %s", (dogID,))
    db.commit()

def get_dog_by_ID(dogID):
    mycursor.execute("SELECT * FROM DOG WHERE ID = %s", (dogID,))
    return mycursor.fetchall()[0]

def add_dog(
name, sex = "M", age = 0, breed = "mix", weight = 0, notes = "", 
neutered = 0, walks = 0, barking = 0, trained = 0, 
training_time = 0, yard_req = 0, friendly = 0, 
energy = 0, attention_req = 0, good_with_pets = 0,
good_with_kids = 0, shedding = 0, size = 0, group):
    mycursor.execute(insertDog, (name, sex, age, breed, weight, notes, neutered, walks, barking, trained, training_time, yard_req, friendly, energy, attention_req, good_with_pets, good_with_kids, shedding, size, group))
    db.commit()


# addDog("James Baxter", "M", 10, "horse", 21, "needs beach ball", 0, 1, 0, -2, -2, 1, 1, 0, -1, -1, -1, -1)
# getDogs()
# deleteDog(7)
# mycursor.close()
print(get_dog_by_ID(9))