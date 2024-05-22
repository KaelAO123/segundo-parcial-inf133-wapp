from database import db
from flask import jsonify
import json
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer,primary_key=True)
    def __init__(self, username, password, role=["user"]):
        self.username = username
        self.password = password
        self.role = json.loads(role)
        db.session.add(self)
        db.session.commit()

    def actualizar_usuario(self, username, password, role):
        if not username:
            self.username = username
        if not password:
            self.password = password
        if not role:
            self.role = json.loads(role)
        
        db.session.add(self)
        db.session.commit()
    
    def eliminar_usuario(self):

        db.session.delete(self)
        db.session.commit()