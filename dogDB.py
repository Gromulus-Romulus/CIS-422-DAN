# # includes
# import mysql.connector
# from flask import Flask


# db = mysql.connector.connect(
# host="ix-dev.cs.uoregon.edu",
# user="guest",
# password="guest",
# port=3144,
# database="dogs")
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'ix-dev.cs.uoregon.edu'
app.config['MYSQL_USER'] = 'guest'
app.config['MYSQL_PASSWORD'] = 'guest'
app.config['MYSQL_DB'] = 'dogs'
 
mysql = MySQL(app)

removeDog = (
    "DELETE * FROM DOG WHERE dogID = %s"
)
insertDog = (
    "INSERT INTO DOG"
    "(name, sex, age, breed, weight, notes, neutered, walks, barking, trained, training_time, yard_requirement, friendly, energy, attention_requirement, good_with_pets, good_with_kids, shedding, size)"
    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)

mycursor = db.cursor(buffered=True)
def getDogs():
    mycursor.execute("SELECT * FROM DOG")
    dogList = []
    for x in mycursor:
        print(x)
        dogList.append(x)
    return dogList
    
def deleteDog(dogID):
    mycursor.execute("DELETE * FROM DOG WHERE dogID = %s", dogID)
    db.commit()

def addDog(
name, sex = "M", age = 0, breed = "mix", weight = 0, notes = "", 
neutered = 0, walks = 0, barking = 0, trained = 0, 
training_time = 0, yard_req = 0, friendly = 0, 
energy = 0, attention_req = 0, good_with_pets = 0,
good_with_kids = 0, shedding = 0, size = 0):
    mycursor.execute(insertDog, (name, sex, age, breed, weight, notes, neutered, walks, barking, trained, training_time, yard_req, friendly, energy, attention_req, good_with_pets, good_with_kids, shedding, size))
    db.commit()

addDog("James Baxter", "M", 10, "horse", 21, "needs beach ball", 0, 1, 0, -2, -2, 1, 1, 0, -1, -1, -1, -1)
getDogs()
