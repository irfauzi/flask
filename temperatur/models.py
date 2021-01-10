
from datetime import datetime
from temperatur import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(pengguna_id):
    return Tpengguna.query.get(int(pengguna_id))


class Tpengguna(db.Model, UserMixin) :
    id= db.Column(db.Integer, primary_key=True)
    nama= db.Column(db.String(50), nullable=False)
    kota= db.Column(db.String(20), nullable=False)
    email= db.Column(db.String(50), unique=True, nullable=False)
    pw= db.Column(db.String(100), nullable=False)
    temp= db.relationship('Ttemperatur', backref='Tpengguna', lazy=True)

    def __repr__(self):
        return f"Tpengguna('{self.nama}', '{self.kota}', '{self.email}', '{self.pw}')"
         


class Ttemperatur(db.Model) :
    id= db.Column(db.Integer, primary_key=True)
    temperatur= db.Column(db.String(10), nullable=False)
    kota= db.Column(db.String(50), nullable=False)
    waktu= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pengguna_id= db.Column(db.Integer, db.ForeignKey('tpengguna.id'))

    def __repr__(self):
        return f"Ttemperatur('{self.temperatur}', '{self.hari}', '{self.waktu}')"   