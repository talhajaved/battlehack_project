from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, DateTimeField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField

class EditProfileForm(Form):
    name = StringField('Real name', validators=[Required(), Length(0, 64)])
    speciality = StringField('Speciality', validators=[Length(0, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    phone_number = StringField('Phone Number', validators=[Length(0, 64)])
    submit = SubmitField('Submit')

class SelectAppointmentForm(Form):
    appointment_time = DateTimeField('Select Appointment Time', validators=[Required()])
    submit = SubmitField('Submit')