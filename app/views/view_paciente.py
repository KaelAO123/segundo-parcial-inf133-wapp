from flask import Flask, render_template

@staticmethod
def lista_pacientes(pacientes):
    return render_template("login.html",title="lista pacientes", patients=pacientes)

@staticmethod
def actualizar_paciente(paciente):
    return render_template("update_pacient.html",title="actualizar paciente", patient=paciente)

@staticmethod
def crear_paciente():
    return render_template("create_patients.html",title="Crear pacientes")