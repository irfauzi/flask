from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from temperatur.models import Tpengguna

class register (FlaskForm):
    nama=StringField('Nama', validators=[DataRequired(), Length(min=4, max=15)])
    kota=StringField('Kota/Kabupaten', validators=[DataRequired(), Length(min=5, max=15)])
    email=EmailField('Email', validators=[DataRequired(), Email() ])
    pw=PasswordField('Password', validators=[DataRequired(), Length(min=3, max=10)])
    cpw=PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('pw')])
    submit=SubmitField('Daftar')

    def validate_email(self, email):
        cekemail=Tpengguna.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError ('Email Sudah Terdaftar')

class login (FlaskForm):
    email=EmailField('Email', validators=[DataRequired() ])
    pw=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Masuk')

class suhu (FlaskForm) :
    temper = IntegerField ('Temperatur Terkini', validators=[DataRequired(), Length(2)])
    kota = StringField ('Lokasi Terkini', validators=[DataRequired(), Length(min=5, max=15)])
    submit = SubmitField ('kirim')