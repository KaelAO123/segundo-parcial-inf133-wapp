from models.model_paciente import Paciente
import views.view_paciente
import requests
from flask import Blueprint, jsonify
from flask_login import LoginManager
from statics.decorator import login_required
import json
paciente_bp = Blueprint("paciente", __name__)
login_manager = LoginManager()
login_manager.init_app()
@paciente_bp.route("/patients")
@login_required
def pacientes():
    pacientes = Paciente.query.all()
    return views.view_paciente.lista_pacientes(pacientes=pacientes)

@paciente_bp.route("/patients/create")
@login_required
def crear_paciente():
    data = requests.json
    name = data.get("name")
    ci = data.get("ci")
    birth_date = data.get("birth_date")
    lastname = data.get("lastname")
    
    if not name or ci is None or not birth_date or not lastname:
        return jsonify({"error":"falta de datos"}),404
    
    Paciente(name=name, birth_date=birth_date, lastname=lastname, ci=ci)
    return pacientes()

@paciente_bp.route("patientes/<id:int>/update")
@login_required
def update_patient():
    data = requests.json
    name = data.get("name")
    ci = data.get("ci")
    birth_date = data.get("birth_date")
    lastname = data.get("lastname")

    Paciente.actualiza_paciente(name=name, birth_date=birth_date,ci=ci,lastname=lastname)
    
    