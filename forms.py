from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email."), Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your first name."), Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email."), Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password")])
    submit = SubmitField('Log in')


class AddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired("Enter an address.")])
    submit = SubmitField('Search')