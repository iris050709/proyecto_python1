from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, create_user, update_user, delete_user, login_user

#obtener todos los usuarios
user_bp = Blueprint('users', __name__)
@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_users()
    return jsonify(user)

#ruta para crear un usuario
@user_bp.route('/', methods = ['POST'])
def user_store():
    data = request.get_json()
    email = data.get('email') 
    name = data.get('name')
    password = data.get('password')
    print(f"NAME {name} --- email {email}")
    new_user = create_user(name, email, password)
    return jsonify(new_user)

# Ruta para actualizar un usuario
@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    updated_user = update_user(user_id, name, email)
    return jsonify(updated_user)

# Ruta para eliminar un usuario
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    result = delete_user(user_id)
    return jsonify(result)

#login
@user_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json();
    return login_user(data['email'], data ['password']);

#http://localhost:5000/users para postman y la accion asi como para el navegador
#activar env\Scripts\activate
#python app.py o flask run para ejecutarse en la terminal
#activar el entorno virtual es env\Scripts\activate