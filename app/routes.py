from flask import Blueprint, render_template, redirect, url_for, flash, request,make_response,jsonify
from flask_login import login_required, login_user, logout_user, current_user
from .models import User, Cliente, Dispositivo
from .database import db
from datetime import date,datetime
from .models import Cliente, reportefinal




# Blueprint en lugar de usar directamente 'app'
main = Blueprint('main', __name__)





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
        nuevo_usuario.set_password(password)  
        nuevo_usuario.set_pin(pin) 
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('main.dashboard')) 
    
    response = make_response(render_template('register.html'), 200)
    # Encabezados para evitar almacenamiento en caché
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response


@main.route('/validate_pin', methods=['POST'])
@login_required
def validate_pin():
    pin = request.form.get('pin')  # Usamos `get()` para evitar errores si la clave no existe

    if pin is None:
        flash('Por favor, ingrese un PIN.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    if current_user.check_pin(pin):  # Asegúrate de que esta función esté bien implementada
        flash('PIN correcto.', 'success')
        return redirect(url_for('main.register_user'))
    else:
        flash('PIN incorrecto.', 'danger')
        return redirect(url_for('main.dashboard'))
 

    
@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard', page_title='Dashboard'))  
    return redirect(url_for('main.login'))  

# Ruta para testear conexión a la base de datos
@main.route('/test_db')
def test_db():
    try:
        usuario = User.query.first() 
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
    hoy = datetime.now()
    fecha = date.today()
    hoy = date.today()
    usuarios_registrados = User.query.all()
    
    
    clientes_hoy = Cliente.query.filter_by(fechaIngreso=hoy).all()
    dispositivos_hoy = Dispositivo.query.filter(Dispositivo.idCliente.in_([cliente.idCliente for cliente in clientes_hoy])).all()
    
    return render_template('dashboard.html', page_title='Dashboard',clientes_hoy=clientes_hoy, dispositivos_hoy=dispositivos_hoy, fecha_hoy=fecha, usuarios=usuarios_registrados, hoy=hoy)
    

# Ruta para login   
    
@main.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('main.inicio'))
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        user = User.query.filter_by(usuario=usuario).first()

       
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
           
            response = make_response(redirect(url_for('main.inicio')))
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response
        else:
            flash('Credenciales inválidas.', 'danger')
            
            response = make_response(redirect(url_for('main.login')))
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response
    
   
    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

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
@main.route('/register_cliente_dispositivo/<int:idCliente>', methods=['GET', 'POST'])
@login_required
def register_cliente_dispositivo(idCliente=None):
    # Si tenemos un idCliente, estamos editando un cliente existente
    if idCliente:
        cliente = Cliente.query.get(idCliente)
        dispositivo = Dispositivo.query.filter_by(idCliente=idCliente).first()
        if not cliente:
            flash('Cliente no encontrado', 'error')
            return redirect(url_for('main.inicio'))

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
        per_recibe = request.form.get('per_recibe')
        clave_tel = request.form.get('clave_tel')
        abono = request.form.get('abono')
        color = request.form.get('color')
        enciende = request.form.get('enciende')
        display_quebrado = request.form.get('display_quebrado')
        tapa_quebrada = request.form.get('tapa_quebrada')
        botones = request.form.get('botones')
        bandeja_sim = request.form.get('bandeja_sim')
        estuche = request.form.get('estuche')
        simcard = request.form.get('simcard')
        estado = request.form.get('estado')

        if idCliente:
            # Editar el cliente existente
            cliente.nombre = nombre
            cliente.apellidos = apellidos
            cliente.nit = nit
            cliente.correo = correo
            cliente.direccion = direccion
            cliente.telefono = telefono
            cliente.fechaIngreso = fechaIngreso
            cliente.estado = estado

            dispositivo.marca = marca
            dispositivo.modelo = modelo
            dispositivo.detalles = detalles
            dispositivo.Imei = IMEI
            dispositivo.per_recibe = per_recibe
            dispositivo.clave_tel = clave_tel
            dispositivo.abono = abono
            dispositivo.color = color
            dispositivo.enciende = enciende
            dispositivo.display_quebrado = display_quebrado
            dispositivo.tapa_quebrada = tapa_quebrada
            dispositivo.botones = botones
            dispositivo.bandeja_sim = bandeja_sim
            dispositivo.estuche = estuche
            dispositivo.simcard = simcard
            db.session.commit()

            flash('Cliente y dispositivo actualizados exitosamente!', 'success')
        else:
            # Crear un nuevo cliente y dispositivo
            nuevo_cliente = Cliente(nombre=nombre, apellidos=apellidos, nit=nit, correo=correo, direccion=direccion, telefono=telefono, fechaIngreso=fechaIngreso, estado=estado)
            db.session.add(nuevo_cliente)
            db.session.commit()

            dispositivo = Dispositivo(idCliente=nuevo_cliente.idCliente, marca=marca, modelo=modelo, detalles=detalles,
                                      Imei=IMEI, per_recibe=per_recibe, clave_tel=clave_tel, abono=abono, color=color,
                                      enciende=enciende, display_quebrado=display_quebrado, tapa_quebrada=tapa_quebrada,
                                      botones=botones, bandeja_sim=bandeja_sim, estuche=estuche, simcard=simcard)
            db.session.add(dispositivo)
            db.session.commit()

            flash('Cliente y dispositivo registrados exitosamente!', 'success')

        return make_response(redirect(url_for('main.inicio')))

    # Si estamos editando, mostramos los datos actuales del cliente y dispositivo
    if idCliente:
        return render_template('cliente.html', page_title='Editar Cliente', cliente=cliente, dispositivo=dispositivo)

    # Si no es edición, simplemente cargamos un formulario vacío para nuevo cliente
    return render_template('cliente.html', page_title='Nuevo Registro', fechaRegistro=date.today())







# Ruta de la página de inicio del dashboard
@main.route('/inicio')
@login_required
def inicio():
    fecha = date.today()
    hoy = date.today()
    
    
    clientes_hoy = Cliente.query.filter_by(fechaIngreso=hoy).all()
    dispositivos_hoy = Dispositivo.query.filter(Dispositivo.idCliente.in_([cliente.idCliente for cliente in clientes_hoy])).all()

    print(clientes_hoy)
    print(dispositivos_hoy)
    
    
    response = make_response(render_template('inicio.html', page_title='Dashboard',clientes_hoy=clientes_hoy, dispositivos_hoy=dispositivos_hoy, fecha_hoy=fecha, hoy=hoy))
    response.headers['Cache-Control'] = 'no-store'
    return response

    

#ruta para cambiar el estado de los registros en inicio.html
@main.route('/actualizar_estado', methods=['GET','POST'])
def actualizar_estado():
    if request.method == 'POST':
        
        idReporte = request.form.get('idReporte')
        idDispositivo = request.form.get('idDispositivo')
        tec_arregla = request.form.get('tec_arregla')
        fechaEntrega = request.form.get('fechaEntrega')
        provedorRepuesto = request.form.get('provedorRepuesto')
        valorRepuesto = request.form.get('valorRepuesto')
        nombreRepuesto = request.form.get('nombreRepuesto')
        valorArreglo = request.form.get('valorArreglo')
        
    
        cliente_id = request.form.get('cliente-id')
        nuevo_estado = request.form.get('estado')


        try:
            cliente = Cliente.query.get(cliente_id)  
            if cliente:
                if cliente.estado == "Entregado":
                    # Si el estado es "Entregado", no permitir la actualización
                    flash('No se puede modificar el estado, ya está marcado como "Entregado".', 'error')
                else:
                    cliente.estado = nuevo_estado
                    db.session.commit()  
                    
                    if nuevo_estado == "entregado":
                        # Convertir la fecha de entrega al formato adecuado
                        fecha_entrega = datetime.strptime(fechaEntrega, '%Y-%m-%d')

                        # Crear un nuevo objeto ReporteFinal
                        reporte = reportefinal(
                            idDispositivo=idDispositivo,
                            tec_arregla=tec_arregla,
                            fechaEntrega=fecha_entrega,
                            provedorRepuesto=provedorRepuesto,
                            valorRepuesto=valorRepuesto,
                            nombreRepuesto=nombreRepuesto,
                            valorArreglo=valorArreglo
                        )

                        # Agregar el reporteFinal a la base de datos
                        db.session.add(reporte)
                        db.session.commit()  # Confirmar la inserción del nuevo reporte

                    flash('Estado actualizado y reporte creado correctamente', 'success')
            else:
                flash('Cliente no encontrado', 'error')

        except Exception as e:
            # Si ocurre un error, revertir los cambios y mostrar el mensaje
            db.session.rollback()
            flash(f'Error al actualizar el estado y el reporte: {str(e)}', 'error')

    return redirect(request.referrer or url_for('main.inicio'))
   
    
    
   

# Ruta para realizar la búsqueda de clientes registrados y sus dispositivos
@main.route('/buscar', methods=['GET','POST'])
@login_required
def buscar():
    query = request.args.get('query', '')

    # Buscar clientes que coincidan con el nombre o NIT
    cliente_results = Cliente.query.filter(
        (Cliente.nombre.ilike(f'%{query}%')) |
        (Cliente.nit.ilike(f'%{query}%')) |
        (Cliente.fechaIngreso.ilike(f'%{query}%'))
    ).all()


    if not cliente_results:
        flash('no se encontro ninguna coincidencia, por favor intente nueva mente','warning' )
    
    response = make_response(render_template('resultado_busqueda.html', page_title='buscar', 
                           cliente_results=cliente_results))
    response.headers['Cache-Control'] = 'no-store'
    return response
    
"""
    # Si se encuentran clientes, buscar dispositivos relacionados con cada cliente
    if cliente_results:
        for dispositivos in cliente_results:
            dispositivos = Dispositivo.query.filter_by(idCliente=Dispositivo.idCliente).all()
            cliente_results=dispositivos  # Agregar los dispositivos encontrados a la lista
"""
    

