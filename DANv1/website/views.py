from flask import Blueprint, render_template, request, url_for, redirect, flash
#from website import website
from website.forms import LoginForm
from website.forms import QuizForm
from website.dog import Dog
from dogdb import *


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

# methods['GET', 'POST'] tells view function to accept GET and POST requests
@views.route('/login', methods=['GET', 'POST'])
def login():
    '''handles logic of login process'''

    # stores wtform in 'form' var
    # wtform defined as LoginForm class in forms.py
    form = LoginForm()

    # checks if form's fields' requirements have been met
    if form.validate_on_submit():
        # flash() makes Flask store the message with the desired format
        flash('Login requested for user {}, password={},remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data))
        # redirect() takes the user to the route argument
        return redirect('/index')

    # if the form hasn't been filled the method will render the given html template
    return render_template("login.html", title='Sign In', form=form)

@views.route('/signup') #methods = ['POST', 'GET']
def start_quiz():
    q = get_questions()
    form = QuizForm()

    # TODO get return data on submission
    return render_template("signup.html", questions=q, form=form)

def get_questions():
    questions = [['question a', ['answer a1', "answer a2",'answer a3']],
    ['question b', ['answer b1', 'answer b2','answer b3']],
    ['question c', ['answer 1c', 'answer 2c','answer c3']]]
    # TODO get actual data for here, 
    # TODO store more info for q and a ids?
    return questions

@views.route('/shelter-login')
def shelter():
    return render_template("shelter-login.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/dogs', methods=["GET", "POST"])
def dogs():
    if request.method == "POST":
        dogid = request.form["value"]
        # print(dogid)
        # dogid = get_dog_by_id(dogid)
        return f"<h1>{dogid}</h1>"
        # return redirect(url_for("views.dog_profile", dogid = dogid))
        # return redirect(url_for("views.dog_profile", dogid = dog))
    d = get_all_dog_ids()
    # d = getDogs()
    # i = 0
    return render_template("all-dogs-test.html", dogs=d)

def get_all_dog_ids():
    # for now these are just their names I made up
    # this should pull just the info we want to display in the all dog view including the id
    d = [["9", "Marvin", "big", "../static/exe-dog.jpeg", "1"], 
    ["3","Fido", "little", "../static/exe-dog3.jpeg", "2"], 
    ["Binger", "medium", "../static/exe-dog.jpeg", "3"], 
    ["Carl", "little", "../static/exe-dog.jpeg", "4"], 
    ["Lindsey", "medium", "../static/exe-dog3.jpeg", "5"],
    ["Annika", "big", "../static/exe-dog.jpeg", "1"], 
    ["Rose", "little", "../static/main-dog.jpeg", "2"], 
    ["Bella", "medium", "../static/exe-dog.jpeg", "3"], 
    ["Bob", "little", "../static/exe-dog.jpeg", "4"], 
    ["Phife", "medium", "../static/exe-dog3.jpeg", "5"]]
    return d

@views.route("/<dogid>")
def dog_profile(dogid):
    # this will call get dog by id and that will return the dog object
    # dogp = get_dog_by_id(dogid)
    # note: can also use an offcanvas element: https://getbootstrap.com/docs/5.2/components/offcanvas/#body-scrolling
    dogp=render_dog_by_id(dogid)
    return render_template("dog-profile.html", dogp = dogp)

# def get_my_dogs(usr_id):
#     return 

@views.route('/test', methods=["POST", "GET"])
def test():
    q = get_questions()
    form = QuizForm()
    if request.method == "POST":
        # flash() makes Flask store the message with the desired format
        flash('Field1: {}, Field2: {}'.format(
            form.myField1.data, form.myField2.data))
        # redirect() takes the user to the route argument
        print('SUCCESS')
        return redirect('/index')

    # TODO get return data on submission
    return render_template("test.html", questions=q, form=form)


@views.route('/dbtest')
def dbtest():
    d = getDogs()
    # dogp = Dog(*d)
    return f'<h1>Test{d}</h1>'

def render_dog_by_id(dogid):

    # dogp = ["Marvin", "big", "../static/exe-dog.jpeg", "1"]
    # TODO this will perform a search function or pull from the db or something
    d = get_dog_by_ID(dogid)
    dogp = Dog(*d)
    return dogp


# TODO use add_url_rule instead? may have to restructure files to access "app"