from flask import Blueprint, render_template, redirect, url_for, flash, request,make_response,jsonify
from flask_login import login_required, login_user, logout_user, current_user
from .models import User, Cliente, Dispositivo
from .database import db
from datetime import date,datetime
from .models import Cliente, reportefinal




# Blueprint main en lugar de usar  'app'
main = Blueprint('main', __name__)





@main.route('/register', methods=['GET', 'POST'])
@login_required
def register_user():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        pin = request.form['pin']  
        

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
    pin = request.form.get('pin')  

    if pin is None:
        flash('Por favor, ingrese un PIN.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    if current_user.check_pin(pin): 
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
    
    
    
    return render_template('dashboard.html', page_title='Dashboard',clientes_hoy=clientes_hoy, dispositivos_hoy=dispositivos_hoy, fecha_hoy=fecha, usuarios=usuarios_registrados, hoy=hoy,show_button=True)
    

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
    cliente = None
    dispositivo = None
    
    # Si hay un idCliente, buscamos al cliente y su dispositivo asociado para editar
    if idCliente:
        cliente = Cliente.query.get(idCliente)
        dispositivo = Dispositivo.query.filter_by(idCliente=idCliente).first()
        if not cliente:
            flash('Cliente no encontrado', 'error')
            return redirect(url_for('main.inicio'))
        if not dispositivo:
            flash('Dispositivo no encontrado', 'error')
            return redirect(url_for('main.inicio'))

    if request.method == 'POST':
        # Datos del cliente
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        nit = request.form.get('nit')
        correo = request.form.get('correo')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        fechaIngreso = request.form.get('fechaIngreso')
        estado = request.form.get('estado')

        # Datos del dispositivo
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        detalles = request.form.get('detalles')
        Imei = request.form.get('Imei')
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

        if idCliente:
            # Si estamos editando un cliente
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
            dispositivo.Imei = Imei
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
            # Si no estamos editando, se crea un nuevo cliente y dispositivo
            nuevo_cliente = Cliente(nombre=nombre, apellidos=apellidos, nit=nit, correo=correo, direccion=direccion,
                                    telefono=telefono, fechaIngreso=fechaIngreso, estado=estado)
            db.session.add(nuevo_cliente)
            db.session.commit()

            dispositivo = Dispositivo(idCliente=nuevo_cliente.idCliente, marca=marca, modelo=modelo, detalles=detalles,
                                      Imei=Imei, per_recibe=per_recibe, clave_tel=clave_tel, abono=abono, color=color,
                                      enciende=enciende, display_quebrado=display_quebrado, tapa_quebrada=tapa_quebrada,
                                      botones=botones, bandeja_sim=bandeja_sim, estuche=estuche, simcard=simcard)
            db.session.add(dispositivo)
            db.session.commit()

            flash('Cliente y dispositivo registrados exitosamente!', 'success')
            
        return redirect(url_for('main.inicio'))

    # Si estamos editando, cargamos los datos del cliente y dispositivo
    return render_template('cliente.html', page_title='Editar Cliente' if idCliente else 'Nuevo Registro',
                           cliente=cliente, dispositivo=dispositivo, show_button=True if not idCliente else False)


@main.route('/get_cliente_info/<int:idCliente>', methods=['GET'])
def get_cliente_info(idCliente):
    try:
        # Obtener la información del cliente
        cliente = Cliente.query.get(idCliente)
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404

        # Obtener los dispositivos del cliente
        dispositivos = Dispositivo.query.filter_by(idCliente=idCliente).all()
        if not dispositivos:
            return jsonify({"error": "Dispositivos no encontrados"}), 404

        # Obtener los IDs de los dispositivos
        dispositivos_ids = [d.idDispositivo for d in dispositivos]

        # Obtener los reportes asociados a esos dispositivos
        reportes = reportefinal.query.filter(reportefinal.idDispositivo.in_(dispositivos_ids)).all()

        # Formatear los datos del cliente
        cliente_data = {
            "idCliente": cliente.idCliente,
            "nombre": cliente.nombre,
            "apellidos": cliente.apellidos,
            "nit": cliente.nit,
            "correo": cliente.correo,
            "direccion": cliente.direccion,
            "telefono": cliente.telefono,
            "fechaIngreso": cliente.fechaIngreso.strftime("%d/%m/%Y") if cliente.fechaIngreso else None,

            
            
        }

        # Formatear los datos de dispositivos
        dispositivos_data = [
            {
                "idDispositivo": dispositivo.idDispositivo,
                "idCliente": dispositivo.idCliente,
                "marca": dispositivo.marca,
                "modelo": dispositivo.modelo,
                "Imei": dispositivo.Imei,
                "color": dispositivo.color,
                "abono": dispositivo.abono,
                "detalles": dispositivo.detalles,
                
            }
            for dispositivo in dispositivos
        ]

        # Formatear los datos de reportes
        reportes_data = [
            {
                "idReporte": reporte.idreporte,
                "idDispositivo": reporte.idDispositivo,
                "tec_arregla": reporte.tec_arregla,
                "provedorRepuesto": reporte.provedorRepuesto,
                "nombreRepuesto": reporte.nombreRepuesto,
                "fechaEntrega": reporte.fechaEntrega.strftime("%d/%m/%Y") if reporte.fechaEntrega else None,
                "valorRepuesto": reporte.valorRepuesto,
                "valorArreglo": reporte.valorArreglo,
            }
            for reporte in reportes
        ]

        # Construir la respuesta
        response = {
            "cliente": cliente_data,
            "dispositivos": dispositivos_data,
            "reportes": reportes_data,
        }

        return jsonify(response), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Error al obtener la información"}), 500


# Ruta de la página de inicio del dashboard

@main.route('/inicio')
@login_required
def inicio():
    fecha = date.today()
    hoy = date.today()
    
    

    
    clientes_hoy = Cliente.query.filter_by(fechaIngreso=hoy).all()
    dispositivos_hoy = Dispositivo.query.filter(Dispositivo.idCliente.in_([cliente.idCliente for cliente in clientes_hoy])).all()
    reportes_hoy= reportefinal.query.filter(reportefinal.idDispositivo.in_([dispositivo.idDispositivo for dispositivo in dispositivos_hoy])).all()
    print(clientes_hoy)
    print(dispositivos_hoy)
    
    
    response = make_response(render_template('inicio.html', 
                                             page_title='Dashboard',
                                             clientes_hoy=clientes_hoy,
                                             dispositivos_hoy=dispositivos_hoy,
                                             reportes_hoy=reportes_hoy,
                                             fecha_hoy=fecha, hoy=hoy,
                                             show_button=False))
    response.headers['Cache-Control'] = 'no-store'
    return response

    

#ruta para cambiar el estado de los registros en inicio.html
@main.route('/actualizar_estado', methods=['GET','POST'])
def actualizar_estado():
    if request.method == 'POST':
        
        
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
                           cliente_results=cliente_results,show_button=True))
    response.headers['Cache-Control'] = 'no-store'
    return response
    


    

