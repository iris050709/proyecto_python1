from models.User import User
from config import db
from flask_jwt_extended import create_access_token

#Lee todos los usuarios 
def get_all_users():
    try:
        return [user.to_dict() for user in User.query.all()]
    except Exception as error:
        print(f"ERROR {error}")

# Create: Crear un nuevo usuario
def create_user(name, email, password):
    try:
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({ 'msg' : "Error al crear usuario"}), 500

# Actualizar un usuario existente
def update_user(user_id, name, email):
    try:
        user = User.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
            return user.to_dict()
        else:
            return {"ERROR": "Usuario no encontrado"}
    except Exception as e:
        print(f"ERROR {e}")
        return {"ERROR": f"Ha ocurrido un error: {str(e)}"}

# Eliminar un usuario
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"menssage": "Usuario eleminado correctamente"}
        else:
            return {"ERROR": "Usuario no encontrado"}
    except Exception as e:
        print(f"ERROR {e}")
        return {"ERROR": f"Ha ocurrido un error: {str(e)}"}
    
#login 
def login_user(email, password):
    user = User.query.filter_by(email=email).first()
        
    if user and user.check_password(password):
        access_token = create_access_token(identity = user.id);
        return jsonify({
            'access_token' : access_token,
            'user':{
                "id" : user.id,
                "name" : user.name,
                "email" : user.email
            }
        })
    return jsonify({ "msg" : "Credenciales invalidas"}), 401