from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    # StringFields take user string input
    # PasswordField take user string input but displays in asterisk form
    # BooleanField creates a on/off toggle button
    # SubmitField creates the button that submits the page contents
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class QuizForm(FlaskForm):
    # INCREDIBLY SCUFFED QUIZ METHOD: create a unique SelectField() for each question
    submit = SubmitField('Submit')
    myField1 = SelectField('Where do you live?', choices=((0,"house"),(1,"apartment"),(2,"houseless")))
    myField2 = SelectField('What kind of outdoor space do you have access to?', choices=((0,"none"), (1,"yard"), (2,"park")))
    myField3 = SelectField('Do you have roommates?', choices=((0,"none"), (1,"1 to 2"), (2,"3-5"), (3,"6-10"), (4,"10<")))
    myField4 = SelectField('Do you have other pets?', choices=((0,"none"), (1,"other dogs"), (2,"cats/other")))
    myField5 = SelectField('Do you have children?', choices=((0,"no"), (1,"planning"), (2,"yes")))
    myField6 = SelectField('How physically active are you?', choices=((0,"not at all"), (1,"moderately (3-4 times/wk)"), (2,"daily")))
    myField7 = SelectField('How much time do you have to play with your dog in addition to daily walks?', choices=((0,"no time"), (1,"2 hours or less"), (2,"all day")))
    myField8 = SelectField('How large would you like your dog to be?', choices=((0,"<30 lbs"), (1,"30-60 lbs"), (2,"60+")))
    myField9 = SelectField('Have you had a dog before?', choices=((0,"yes"), (1,"no")))
    myField10 = SelectField('How much time will your dog have to spend alone?', choices=((0,"very little"), (1,"2-8 hrs"), (2,"8+ hrs")))
    myField11 = SelectField('How well would you like your new dog to be trained?', choices=((0,"none"), (1,"moderately"), (2,"highly")))
    myField12 = SelectField('How much time do you have to train your dog?', choices=((0,"none"), (1,"0-2hrs per week"), (2,">2hrs per week")))
    myField13 = SelectField('How friendly/protective do you want your dog to be?', choices=((0,"very protective"), (1,"moderately protective"), (2, "not too much of either"), (3,"moderately friendly"),(4,"very friendly")))
    myField14 = SelectField('How often can you groom your dog?', choices=((0,"never"), (1,"weekly"), (2,"daily")))
    myField15 = SelectField('How much shedding do you want from your dog?', choices=((0,"minimal"), (1,"moderate"), (2,"don't care")))
    myField16 = SelectField('How much barking do you expect from your dog?', choices=((0,"minmal "), (1,"moderate"), (2,"don't care")))



#, validators=[DataRequired()]