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
    



# Modelo de Dispositivo
class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    idDispositivo = db.Column(db.BigInteger, primary_key=True)
    idCliente = db.Column(db.BigInteger, db.ForeignKey('cliente.idCliente'), nullable=False)
    marca = db.Column(db.String(45), nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    detalles = db.Column(db.String(255), nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)
    IMEI = db.Column(db.String(20), nullable=False)
    per_recibe= db.Column(db.String(45), nullable=False)
    clave_tel=db.Column(db.String(45), nullable=False)
    abono= db.Column(db.Numeric(10, 2), nullable=False)

# Modelo de usuario para la autenticación
class User(UserMixin, db.Model):
    __tablename__ = 'user'  # Nombre de la tabla en MySQL
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Cambié el tamaño del campo
    pin = db.Column(db.String(20), nullable=False)  # Campo para el PIN

    def set_password(self, password):
        self.password = generate_password_hash(password)  # Hashea la contraseña

    def check_password(self, password):
        return check_password_hash(self.password, password)

    
    def set_pin(self, pin):
        self.pin = pin  # Almacena el PIN directamente (puedes hashearlo si lo deseas)

    def check_pin(self, pin):
        return self.pin == pin
    

    def __repr__(self):
        return f"user('{self.usuario}')"