from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class RegisterForm(FlaskForm):
    ClientId=StringField(label='CLIENT ID:',validators=[DataRequired(),Length(min=2,max=10)])
    ClientName=StringField(label='CLIENT NAME:',validators=[DataRequired()])
    ClientType=StringField(label='Transmission Type:',validators=[DataRequired()])
    ClientBSI=StringField(label='BSI:',validators=[DataRequired()])
    ClientStatus=StringField(label='Status:',validators=[DataRequired()])
    Submit=SubmitField(label='Submit')

class SearchForm(FlaskForm):
    ClientId=StringField(label='Enter the CLIENT ID:',validators=[DataRequired()])
    Search=SubmitField(label='Search')