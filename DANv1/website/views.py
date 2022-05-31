from flask import Blueprint, render_template, request, url_for, redirect

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

@views.route('/dogs', methods=["GET", "POST"])
def dogs():
    if request.method == "POST":
        dogid = request.form["value"]
        # dog = "Marvin"
        dogp = get_dog_by_id(dogid)
        return render_template("dog-profile.html", dogp=dogp)
        # return redirect(url_for("views.dog_profile", dogid = dog))
    d = get_all_dog_ids()
    # i = 0
    return render_template("all-dogs.html", dogs=d)

def get_all_dog_ids():
    # for now these are just their names I made up
    d = [["Marvin", "big", "../static/exe-dog.jpeg", "1"], 
    ["Fido", "little", "../static/exe-dog3.jpeg", "2"], 
    ["Binger", "medium", "../static/exe-dog.jpeg", "3"], 
    ["Carl", "little", "../static/exe-dog.jpeg", "4"], 
    ["Lindsey", "medium", "../static/exe-dog3.jpeg", "5"]]
    return d

# def get_my_dogs(usr_id):
#     return 

# @views.route('/<dogid>')
# def dog_profile(dogid):
#     dogp = get_dog_by_id(dogid)
#     # TODO replace with get dog by id
#     return render_template("dog-profile.html", dogp = dogp)

# @views.route('/<dogid>')
# def dog_profile(dogid):
#     dogp = ["Marvin", "big", "../static/exe-dog.jpeg"]
#     # TODO replace with get dog by id
#     return render_template("dog-profile.html", dogp)

@views.route('/test')
def test():
    q = get_questions()
    return render_template("test.html", test=q)

# TODO store dogs as objects in a csk map?
# TODO or have a db call using dogid that returns a dog object or dict or something

def get_dog_by_id(dogid):
    dogp = ["Marvin", "big", "../static/exe-dog.jpeg", "1"]
    return dogp


# TODO use add_url_rule instead? may have to restructure files to access "app"