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
    myField1 = SelectField('Question1', choices=("Answer1a","Answer1b","Answer1c"))
    myField2 = SelectField('Question2', choices=("Answer2a", "Answer2b", "Answer3c"))

#, validators=[DataRequired()]