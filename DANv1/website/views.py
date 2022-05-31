from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/signup')
def start_quiz():
    q = get_questions()
    return render_template("signup.html", questions=q)

def get_questions():
    questions = [['question a', ['answer a1', "answer a2"]],['question b', ['answer b1', 'answer b2']],['question c', ['answer 1c', 'answer 2c']]]
    # TODO get actual data for here
    return questions

@views.route('/for-shelters')
def shelter():
    return render_template("shelter-login.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/dogs')
def dogs():
    return render_template("dogs.html")

@views.route('/test')
def test():
    q = get_questions()
    return render_template("test.html", questions=q)


# TODO use add_url_rule instead? may have to restructure files to access "app"