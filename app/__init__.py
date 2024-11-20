from flask import Flask
from flask_login import LoginManager
from .database import db
 

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicializar las extensiones
    db.init_app(app)
    login_manager.init_app(app)
    
   
    # Manejar la importación del modelo con un bloque try-except
    

    # Importar el modelo User después de inicializar la db
    from .models import User

    # Definir el user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Recupera el usuario por ID
    
    

    # Registrar los blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
