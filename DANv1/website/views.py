from flask import Blueprint, render_template, request, url_for, redirect, flash
#from website import website
from website.forms import LoginForm
from website.forms import QuizForm
from website.dogdb import *
from website.dog import Dog
from website.filter import magic_filter_function

masterList = []

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

@views.route('/signup', methods = ['POST', 'GET'])
def start_quiz():

    global masterList
    # reset masterlist
    masterList = []

    form = QuizForm()
    if request.method == 'POST':
        # flash() makes Flask store the message with the desired format

        masterList.append(int(form.myField6.data))
        masterList.append(int(form.myField16.data))
        masterList.append(int(form.myField11.data))
        masterList.append(int(form.myField2.data))
        masterList.append((int(form.myField3.data) + int(form.myField13.data))//2)
        masterList.append((int(form.myField6.data) + int(form.myField7.data) + int(form.myField2.data)
                           + int(form.myField10.data) + int(form.myField1.data))//2)
        masterList.append(int(form.myField7.data))
        masterList.append(int(form.myField4.data))
        masterList.append(int(form.myField5.data))
        masterList.append((int(form.myField15.data) + int(form.myField14.data)) // 2)
        masterList.append((int(form.myField1.data) + int(form.myField8.data)) // 2)

        print(masterList)
        # masterList.clear()

        # ---------------------------------
        # masterList holds all quiz responses
        global match_ids
        match_ids = magic_filter_function(masterList)

        # match_ids = ["3","9","12"]
        # convert list of ids to list of dog tuples
        """dogs=[]
        for id in match_ids:
            print("looking for "+ str(id))
            d = get_dog_by_ID(id)
            if d != 0:
                dogs.append(d)"""

        # TESTING use to show dogs from junk data


        return redirect(url_for("views.my_dogs"))
        #return render_template("all-dogs.html", dogs=dogs)

        # TESTING Use this to show the quiz results after pressing submit button
#         return f"<h1>{masterList}{match_ids}</h1>"
        
        # return redirect(url_for("views.my_dogs", match_ids= match_ids))

    # TODO get return data on submission

    return render_template("signup.html", questions=q, form=form)


def get_questions():
    questions = [['question a', ['answer a1', "answer a2",'answer a3']],
    ['question b', ['answer b1', 'answer b2','answer b3']],
    ['question c', ['answer 1c', 'answer 2c','answer c3']]]
    # TODO get actual data for here, 
    # TODO store more info for q and a ids?
    return questions

# TODO add login here --> dashboard that allows upload to db?
@views.route('/shelter-login')
def shelter():
    return render_template("shelter-login.html")

# TODO add more content to this page
@views.route('/about')
def about():
    return render_template("about.html")

# All Dog View
@views.route('/dogs', methods=["GET", "POST"])
def dogs():
    if request.method == "POST":
        dogid = request.form["id"]
        return redirect(url_for("views.dog_profile", dogid = dogid))
        # return redirect(url_for("views.dog_profile", dogid = dog))
    dogs = get_dogs()
    # i = 0
    return render_template("all-dogs.html", dogs=dogs)

# TODO add some kind of validation?
# TODO have url route be /<username>
@views.route('/my-dogs', methods=["GET", "POST"])
def my_dogs():
    global match_ids
    if request.method == "POST":
        dogid = request.form["id"]
        return redirect(url_for("views.dog_profile", dogid = dogid))
    
    dogs = []
    for id in match_ids:
        d = get_dog_by_ID(id)
        dogs.append(d)
    match_ids.clear()
    return render_template("all-dogs.html", dogs=dogs)

# Individual Dog Full Profile View
@views.route("/<dogid>")
def dog_profile(dogid):
    dog = get_dog_by_ID(dogid)
    dogp = Dog(*dog)
    # note: can also use an offcanvas element: https://getbootstrap.com/docs/5.2/components/offcanvas/#body-scrolling
    return render_template("dog-profile.html", dogp = dogp)



@views.route('/test', methods=["POST", "GET"])
def test():
    global masterList
    q = get_questions()
    form = QuizForm()
    if request.method=='POST':
        # flash() makes Flask store the message with the desired format
        flash('Field1: {}, Field2: {}'.format(
            form.myField1.data, form.myField2.data))
        masterList.append(form.myField1.data)
        masterList.append(form.myField2.data)
        masterList.append(form.myField3.data)
        masterList.append(form.myField4.data)
        masterList.append(form.myField5.data)
        masterList.append(form.myField6.data)
        masterList.append(form.myField7.data)
        masterList.append(form.myField8.data)
        masterList.append(form.myField9.data)
        masterList.append(form.myField10.data)
        masterList.append(form.myField11.data)
        masterList.append(form.myField12.data)
        masterList.append(form.myField13.data)
        masterList.append(form.myField14.data)
        masterList.append(form.myField15.data)
        masterList.append(form.myField16.data)
        # redirect() takes the user to the route argument
        print(masterList)
        masterList.clear()
        return redirect('/index')

    # TODO get return data on submission
    return render_template("test.html", questions=q, form=form)
