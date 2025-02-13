from flask import request,jsonify
import os
from user_app.services.user_service import UserService
from user_app.views.user_view import UserView
from werkzeug.utils import secure_filename
from shared.utils.db_utils import db
from shared.models.user_model import User



class UserController:
    @staticmethod
    def get_all_users():
        users = UserService.get_all_users()
        return UserView.render_users(users), 200

    @staticmethod
    def get_user(username):
        user = UserService.get_user_by_username(username)
        if not user: # if user is None:
            return UserView.render_error('User not found'), 404
        return UserView.render_user(user), 200

    @staticmethod
    def create_user():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name', '')
        bio = data.get('bio', '')

        user = UserService.create_user(username, email, password, full_name, bio)
        return UserView.render_success('User created successfully', user.user_id), 201

    @staticmethod
    def login_user():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = UserService.verify_user(username, password)
        if user:
            return UserView.render_success('Login successful', user.user_id), 200
        return UserView.render_error('Invalid username or password'), 401
    
    
    @staticmethod
    def update_user(user_id):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name')
        bio = data.get('bio')
        linkedin_url = data.get('linkedin_url')
        github_url = data.get('github_url')
        
        user=UserService.update_user(user_id, username, email, password, full_name, bio, linkedin_url, github_url)
        if user:
            return UserView.render_success('User updated successfully', user.user_id), 200
        return UserView.render_error('User not found'), 404
            
    
    
    @staticmethod
    def upload_image():
        # Check if the file part is present in the request
        if 'file' not in request.files:
            return UserView.render_error('No file part'), 400

        # Retrieve the file and user_id from the request
        file = request.files['file']
        user_id = request.form.get('user_id')
        
        # Validate the user_id
        if not user_id:
            return UserView.render_error('No user_id provided'), 400
        
        # Call the UserService upload_image method
        image_response = UserService.upload_image(file, user_id)
        
        # Handle response from upload_image method
        if image_response == 1:
            return UserView.render_error('No selected file'), 400

        if image_response == 2:
            return UserView.render_error('File type not allowed'), 400

        if image_response == 3:  
            return UserView.render_error('User not found'), 404

        if image_response == 4:
            return UserView.render_error("An error occurred while saving the file abcd:"), 500

        # Success case: return the success message with the uploaded file's URL
        return UserView.render_success(f"User ID '{user_id}' uploaded file '{image_response}' successfully!"), 200
    
    
    @staticmethod
    def add_user_links(user_id):
        linkedin_url = request.json.get('linkedin_url')
        github_url = request.json.get('github_url')

       
        if linkedin_url and not linkedin_url.startswith("https://www.linkedin.com/"):
            return jsonify({"error": "Invalid LinkedIn URL"}), 400
        if github_url and not github_url.startswith("https://github.com/"):
            return jsonify({"error": "Invalid GitHub URL"}), 400

        response, status_code = UserService.add_user_links(user_id, linkedin_url, github_url)
        return jsonify(response)
    
    
     
    @staticmethod    
    def update_live_location():
        # Extract data from the request
        data = request.json
        user_id = data.get('user_id')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if not user_id or latitude is None or longitude is None:
            return jsonify({"error": "Missing parameters"}), 400


        user = User.query.get(user_id)
        if user:
            user.live_location_latitude = latitude
            user.live_location_longitude = longitude
            db.session.commit()
            return jsonify({"message": "Live location updated successfully"}), 200

        return jsonify({"error": "User not found"}), 404
    
    @staticmethod
    def get_user_location(user_id):
        location_data = UserService.get_user_location(user_id)
        if location_data:
            return jsonify(location_data), 200
        return jsonify({"error": "User not found"}), 404
    
    @staticmethod
    def update_current_location():
        data = request.json
        user_id = data.get('user_id')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if not user_id or latitude is None or longitude is None:
            return jsonify({"error": "Missing parameters"}), 400

        user = UserService.update_current_location(user_id, latitude, longitude)
        if user:
            return jsonify({"message": "Current location updated successfully"}), 200

        return jsonify({"error": "User not found"}), 404
    
    @staticmethod
    def get_user_current_location(user_id):
        location = UserService.get_current_location(user_id)
        if location:
            return jsonify(location), 200
        return jsonify({"error": "User not found"}), 404