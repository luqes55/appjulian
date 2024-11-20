from flask import Blueprint, render_template, redirect, url_for, flash, request,make_response
from flask_login import login_required, login_user, logout_user, current_user
from .models import User, Cliente, Dispositivo
from .database import db
from datetime import date



# Blueprint en lugar de usar directamente 'app'
main = Blueprint('main', __name__)


#ruta para registrar un nuevo usuario

@main.route('/register', methods=['GET', 'POST'])
@login_required
def register_user():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        pin = request.form['pin']  # Captura el PIN

        # Verificar si el usuario ya existe
        existing_user = User.query.filter_by(usuario=usuario).first()
        if existing_user:
            flash('El usuario ya existe.', 'danger')
            return redirect(url_for('main.register_user'))

        # Crear un nuevo usuario
        nuevo_usuario = User(usuario=usuario)
        nuevo_usuario.set_password(password)  # Hashear la contraseña
        nuevo_usuario.set_pin(pin)  # Guardar el PIN
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario registrado exitosamente.', 'success')
        return make_response(redirect(url_for('main.register_user')), 200) 
        
         # Respuesta con código 200

    return make_response(render_template('register.html', page_title='Registrar usuario'), 200)

@main.route('/validate_pin', methods=['POST'])
@login_required
def validate_pin():
    pin = request.form['pin']

    # Lógica para validar el PIN almacenado en la base de datos
    if current_user.check_pin(pin):  # Utiliza el método check_pin que definiste en tu modelo User
        # El PIN es correcto, redirigir a la ruta de registro
        return redirect(url_for('main.register_user'))
    else:
        # El PIN es incorrecto, redirigir a la página de inicio (dashboard) con un mensaje de error
        flash('PIN incorrecto', 'danger')
        return redirect(url_for('main.dashboard'))








@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard', page_title='Dashboard'))  # Redirigir al dashboard si autenticado
    return redirect(url_for('main.login'))  # Redirigir al login si no autenticado

# Ruta para testear conexión a la base de datos
@main.route('/test_db')
def test_db():
    try:
        usuario = User.query.first()  # Consulta a la tabla `User`
        if usuario:
            return f"Conexión exitosa. Primer usuario: {usuario.usuario}"
        else:
            return "Conexión exitosa, pero no hay usuarios en la tabla."
    except Exception as e:
        return f"Error al conectarse a la base de datos: {e}"

# Ruta del dashboard
@main.route('/dashboard')
@login_required
def dashboard():
    response = make_response(render_template('dashboard.html', page_title='Dashboard'))
    response.headers['Cache-Control'] = 'no-store'
    return response

# Ruta para login

@main.route('/login', methods=['GET', 'POST'])
def login():
    
    
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        user = User.query.filter_by(usuario=usuario).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            response = make_response(redirect(url_for('main.dashboard')))
            return response
        else:
            flash('Credenciales inválidas.', 'danger')
            response = make_response(redirect(url_for('main.login')))
            return response
    return make_response(render_template('login.html'))

# Ruta para cerrar sesión
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'success')
    response = make_response(redirect(url_for('main.login')))
    return response

# Ruta para registrar cliente y dispositivo

@main.route('/register_cliente_dispositivo', methods=['GET', 'POST'])
@login_required
def register_cliente_dispositivo():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        nit = request.form.get('nit')
        correo = request.form.get('correo')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        detalles = request.form.get('detalles')
        fechaIngreso = request.form.get('fechaIngreso')
        IMEI = request.form.get('Imei')
        per_recibe= request.form.get('per_recibe')
        clave_tel=request.form.get('clave_tel')
        abono=request.form.get('abono')
        color=request.form.get('color')
        enciende=request.form.get('enciende')
        display_quebrado=request.form.get('display_quebrado')
        tapa_quebrada=request.form.get('tapa_quebrada')
        botones=request.form.get('botones')
        bandeja_sim=request.form.get('bandeja_sim')
        estuche=request.form.get('estuche')
        simcard=request.form.get('simcard')
        estado=request.form.get('estado')

        # Validación de campos
   
        
    
        # Guardar cliente y dispositivo en la base de datos
        nuevo_cliente = Cliente(nombre=nombre, apellidos=apellidos, nit=nit, correo=correo, direccion=direccion, telefono=telefono, fechaIngreso=fechaIngreso, )
        db.session.add(nuevo_cliente)
        db.session.commit()

        dispositivo = Dispositivo(idCliente=nuevo_cliente.idCliente, marca=marca, modelo=modelo, detalles=detalles,
                                  Imei=IMEI, per_recibe=per_recibe, clave_tel=clave_tel, abono=abono,color=color, enciende=enciende, 
                                  display_quebrado=display_quebrado, tapa_quebrada=tapa_quebrada, botones=botones, bandeja_sim=bandeja_sim, estuche=estuche, simcard=simcard, estado=estado)
        db.session.add(dispositivo)
        db.session.commit()

        flash('Cliente y dispositivo registrados exitosamente!', 'success')
        return make_response(redirect(url_for('main.inicio')))

    return make_response(render_template('cliente.html', page_title='Registro', fechaRegistro=date.today()))

# Ruta de la página de inicio del dashboard
@main.route('/inicio')
@login_required
def inicio():
    hoy = date.today()
    clientes_hoy = Cliente.query.filter_by(fechaIngreso=hoy).all()
    dispositivos_hoy = Dispositivo.query.filter_by(idCliente=hoy).all()
    
    response = make_response(render_template('inicio.html', clientes_hoy=clientes_hoy, dispositivos_hoy=dispositivos_hoy, page_title='inicio'))
    response.headers['Cache-Control'] = 'no-store'
    return response


# Ruta para realizar la búsqueda de clientes registrados y sus dispositivos
@main.route('/buscar', methods=['GET','POST'])
@login_required
def buscar():
    query = request.args.get('query', '')

    # Buscar clientes que coincidan con el nombre o NIT
    cliente_results = Cliente.query.filter(
        (Cliente.nombre.ilike(f'%{query}%')) |
        (Cliente.nit.ilike(f'%{query}%'))
    ).all()


    if not cliente_results:
        flash('no se encontro ninguna coincidencia, por favor intente nueva mente','warning' )
    
    
    

    # Si se encuentran clientes, buscar dispositivos relacionados con cada cliente
    if cliente_results:
        for dispositivos in cliente_results:
            dispositivos = Dispositivo.query.filter_by(idCliente=Dispositivo.idCliente).all()
            cliente_results=dispositivos  # Agregar los dispositivos encontrados a la lista

    return render_template('resultado_busqueda.html', page_title='Buscar', 
                           cliente_results=cliente_results)

