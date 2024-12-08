from sqlalchemy import Enum
from .database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#modelo de las tablas de la base de datos mysql
# Modelo de Cliente

class Cliente(db.Model):
    __tablename__ = 'cliente'
    idCliente = db.Column(db.BigInteger, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(45), nullable=False)
    nit = db.Column(db.BigInteger, nullable=False)
    correo = db.Column(db.String(65), nullable=False)
    direccion = db.Column(db.String(65), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)
    estado=db.Column(Enum('pendiente','entregado', name='estado_enum'), nullable=False)

    dispositivos = db.relationship('Dispositivo', backref='cliente', lazy=True)
# Modelo de Dispositivo
class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    idDispositivo = db.Column(db.BigInteger, primary_key=True)
    idCliente = db.Column(db.BigInteger, db.ForeignKey('cliente.idCliente'), nullable=False)
    marca = db.Column(db.String(45), nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    detalles = db.Column(db.String(255), nullable=False)
    Imei = db.Column(db.String(15), nullable=True)
    per_recibe= db.Column(db.String(45), nullable=False)
    clave_tel=db.Column(db.String(45), nullable=False)
    abono= db.Column(db.Numeric(10, 2), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    enciende = db.Column(db.String(3), nullable=False)  # asumiendo que 'si' o 'no'
    display_quebrado = db.Column(db.String(10), nullable=True)  # asumiendo que 'si' o 'no'
    tapa_quebrada = db.Column(db.String(10), nullable=False)  # 'buena' o 'quebrada'
    botones = db.Column(db.String(3), nullable=False)  # asumiendo que 'si' o 'no'
    simcard = db.Column(db.String(3), nullable=False)  # asumiendo que 'si' o 'no'
    estuche = db.Column(db.String(3), nullable=False)  # asumiendo que 'si' o 'no'
    bandeja_sim = db.Column(db.String(3), nullable=False)  # asumiendo que 'si' o 'no'
   
    
# Modelo de usuario para la autenticación
class User(UserMixin, db.Model):
    __tablename__ = 'user'  
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  
    pin = db.Column(db.String(20), nullable=False)  

     # Hashea la contraseña
    def set_password(self, password):
        self.password = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password, password)

    
    def set_pin(self, pin):
        self.pin = pin  

    def check_pin(self, pin):
        return self.pin == pin
    
    def __repr__(self):
        return f'<User {self.usuario}>'


class reportefinal(db.Model):
    __tablename__ = 'reportefinal'
    idreporte=db.Column(db.BigInteger, primary_key=True)
    idDispositivo = db.Column(db.BigInteger, db.ForeignKey('dispositivo.idDispositivo'), nullable=False)
    tec_arregla=db.Column(db.String(20), nullable=False)
    fechaEntrega=db.Column(db.Date, nullable=False)
    provedorRepuesto=db.Column(db.String(30), nullable=False)
    valorRepuesto=db.Column(db.Numeric(10, 2), nullable=False)
    nombreRepuesto=db.Column(db.String(20), nullable=False)
    valorArreglo=db.Column(db.Numeric(10, 2), nullable=False)
    
    dispositivo = db.relationship('Dispositivo', backref='reportefinal', lazy=True)