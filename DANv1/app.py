from flask import Flask, render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'ix-dev.cs.uoregon.edu'
app.config['MYSQL_PORT'] = 3144
app.config['MYSQL_USER'] = 'guest'
app.config['MYSQL_PASSWORD'] = 'guest'
app.config['MYSQL_DB'] = 'dogs'
 
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM DOG")
    dogs = cur.fetchall()
    print(dogs)
    return "done."

if __name__=="__main__":
    app.run()