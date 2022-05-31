from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/signup') #methods = ['POST', 'GET']
def start_quiz():
    q = get_questions()
    # TODO get return data on submission
    return render_template("signup.html", questions=q)

def get_questions():
    questions = [['question a', ['answer a1', "answer a2"]],
    ['question b', ['answer b1', 'answer b2']],
    ['question c', ['answer 1c', 'answer 2c']]]
    # TODO get actual data for here, 
    # TODO store more info for q and a ids?
    return questions

@views.route('/for-shelters')
def shelter():
    return render_template("shelter-login.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/dogs')
def dogs():
    d = get_all_dog_ids()
    # i = 0
    return render_template("all-dogs.html", dogs=d)

def get_all_dog_ids():
    # for now these are just their names I made up
    d = [["Marvin", "big", "../static/exe-dog.jpeg"], 
    ["Fido", "little", "../static/exe-dog3.jpeg"], 
    # ["Binger", "medium", "../static/exe-dog.jpeg"], 
    ["Carl", "little", "../static/exe-dog.jpeg"], 
    ["Lindsey", "medium", "../static/exe-dog3.jpeg"]]
    return d

# def get_my_dogs(usr_id):
#     return 

@views.route('/test')
def test():
    q = get_questions()
    return render_template("test.html", test=q)


# TODO use add_url_rule instead? may have to restructure files to access "app"