from app import db
from flask.ext.login import UserMixin
from datetime import datetime

class Doctor(UserMixin, db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    phone_number = db.Column(db.String(64), nullable=True)
    speciality = db.Column(db.String(64), nullable=True)
    location = db.Column(db.String(64), nullable=True)
    appointments = db.relationship('Appointment', backref='doctor', lazy='dynamic')


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.String(64), nullable=True)
    age = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    appointments = db.relationship('Appointment', backref='patient', lazy='dynamic')
    phone_calls = db.relationship('PatientPhoneCalls', backref='patient', lazy='dynamic')

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed, randit
        import forgery_py

        seed()
        for i in range(count):
            u = Patient(email=forgery_py.internet.email_address(),
                     name=forgery_py.name.full_name(),
                     phone_number=forgery_py.forgery.address.phone(),
                     gender=forgery_py.forgery.personal.gender(),
                     age=randint(20, 40))
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(64), nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    appointment_time = db.Column(db.DateTime)
    phone_calls = db.relationship('PatientPhoneCalls', backref='appointments', lazy='dynamic')

class PatientPhoneCalls(db.Model):
    __tablename__ = 'phone_calls'
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    case_severity = db.Column(db.String(64), nullable=True)
    symptoms = db.Column(db.String(64), nullable=True)
    status = db.Column(db.String(64), nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

