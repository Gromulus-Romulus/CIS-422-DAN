'''
this file connects the front-end Flask webpage to the
back-end mysql database holding all our information
'''
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
    (name, photo, sex, age, breed, grouping, weight, notes, fixed, walks, barking, trained, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
)

mycursor = db.cursor(buffered=True)
def get_dogs():
    '''Retrieves the info from the dog database
    and puts it in a list'''
    mycursor.execute("SELECT * FROM DOG")
    dogList = []
    for x in mycursor:
        # print(x)
        dogList.append(x)

    return dogList
    
def delete_dog(dogID):
    '''This function deletes a dog entry from the database'''
    mycursor.execute("DELETE FROM DOG WHERE ID = %s", (dogID,))
    db.commit()

def get_dog_by_ID(dogID):
    '''This function retrieves a dog from database
    specific to the ID passed into the function'''
    mycursor.execute("SELECT * FROM DOG WHERE ID = %s", (dogID,))
    data = mycursor.fetchall()
    if data:
        return data[0]
    else:
        return 0

def add_dog(
name, photo, sex, age, breed, grouping, weight, notes, 
fixed, walks, barking, trained, yard_req, friendly, 
energy, attention_req, good_with_pets,
good_with_kids, shedding, size):
    '''This function adds a dog entry to the database'''
    mycursor.execute(insertDog, (name, photo, sex, age, breed, grouping, weight, notes, fixed, walks, barking, trained, yard_req, friendly, energy, attention_req, good_with_pets, good_with_kids, shedding, size,))
    db.commit()



