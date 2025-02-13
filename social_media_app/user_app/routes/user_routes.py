from flask import Blueprint,request
from user_app.controllers.user_controller import UserController


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/users', methods=['GET'])
def get_all_users():
    print("ss")
    return UserController.get_all_users()

@user_bp.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    return UserController.get_user(username)

@user_bp.route('/api/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/api/users/login', methods=['POST'])
def login_user():
    return UserController.login_user()


@user_bp.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return UserController.update_user(user_id)


@user_bp.route('/api/users/upload_image', methods=['POST'])
def upload_image():
    return UserController.upload_image()

@user_bp.route('/api/users/<int:user_id>/add_links', methods=['POST'])
def add_user_links(user_id):
    return UserController.add_user_links(user_id)

@user_bp.route('/api/get-location/<int:user_id>', methods=['GET'])
def get_location(user_id):
    return UserController.get_user_location(user_id)
    
@user_bp.route('/api/update-location', methods=['POST'])
def update_live_location():
    return UserController.update_live_location()

@user_bp.route('/api/update-current-location', methods=['POST'])
def update_current_location_route():
    return UserController.update_current_location()

@user_bp.route('/api/get-current-location/<int:user_id>', methods=['GET'])
def get_current_location_route(user_id):
    return UserController.get_user_current_location(user_id)