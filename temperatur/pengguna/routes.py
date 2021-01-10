from flask import Flask, render_template, redirect, url_for, Blueprint, flash
from temperatur.pengguna.forms import register, login, suhu
from temperatur.models import Tpengguna, Ttemperatur
from temperatur import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

rregister = Blueprint('rregister', __name__)

@rregister.route('/')
def home():
    return render_template ('home.html')

@rregister.route('/register', methods=['GET', 'POST'])
def registerP():
    form=register()
    if form.validate_on_submit():
        pw_hash=bcrypt.generate_password_hash(form.pw.data).decode('UTF-8')
        add_pengguna=Tpengguna(nama=form.nama.data, kota=form.kota.data, email=form.email.data, pw=pw_hash)
        db.session.add(add_pengguna)
        db.session.commit()
        flash(f'{form.nama.data} berhasil ditambahkan', 'warning')
        return redirect (url_for('rregister.loginP'))
    return render_template ('register.html', form=form)

@rregister.route('/login', methods=['GET', 'POST'])
def loginP():
    if current_user.is_authenticated:
        return redirect(url_for('rregister.akunP'))
    form=login()
    if form.validate_on_submit():
        cekemail=Tpengguna.query.filter_by(email=form.email.data).first()
        if cekemail and bcrypt.check_password_hash(cekemail.pw, form.pw.data):
            login_user(cekemail)
            flash('Selamat Datang', 'warning')
            return redirect (url_for('rregister.akunP'))
        else:
            flash('Login Gagal, Periksa kembali Email dan Password', 'danger')
    return render_template ('login.html', form=form)


@rregister.route('/about')
def about():
    return render_template ('about.html')

@rregister.route('/akunP')
@login_required
def akunP():
    form=suhu()
    return render_template ('akun.html', form=form)

@rregister.route('/logoutP')
def logoutP():
    logout_user()
    return redirect(url_for('rregister.home'))


@rregister.route('/temper', methods=['GET', 'POST'])
def temp():
    form=suhu()
   # if form.validate_on_submit():
        
    return render_template('temperatur.html', form=form)