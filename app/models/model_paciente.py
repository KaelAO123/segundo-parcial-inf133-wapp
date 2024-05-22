
from database import db
import flask_sqlalchemy
from flask import jsonify, request, redirect, url_for
import json
class Paciente(db.Model):
    __tablename__ = "paciente"
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100),nullable=False)
    lastname = db.column(db.String(100),nullable=False)
    ci = db.column(db.Integer, nullable= False)
    birth_date = db.column(db.String(100),nullable=False)

    def __init__(self, name, lastname, ci, birth_date):
        self.name = name
        self.lastname = lastname
        self.ci = ci
        self.birth_date = birth_date
        db.session.add(self)
        db.session.commit()

    def actualiza_paciente(self, name,lastname,ci,birth_date):
        if not name:
            self.name = name
        if not lastname:
            self.lastname = lastname
        if ci is not None:
            self.ci = ci
        if not birth_date:
            self.birth_date
        db.session.add(self)
        db.session.commit()
    
    def eliminar_paciente(id):
        paciente = Paciente.query.get(id)
        db.session.delete(paciente)
        db.session.commit()

    @staticmethod
    def buscar_paciente(id):
        paciente = Paciente.query.get(id)
        return paciente
    

    