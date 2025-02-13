from shared.models.user_model import User
from shared.utils.db_utils import db
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials
from io import BytesIO #substituting non memory files during development
from firebase_admin import storage
import uuid
from datetime import datetime

cred = credentials.Certificate(r"C:\Users\khush\OneDrive\Desktop\version_2\social-media-app-61969-firebase-adminsdk-qyckq-e520fa4dcf.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'social-media-app-61969.appspot.com'
})


def to_dict(status, message, **kwargs):
        response = {"status": status, "message": message}
        response.update(kwargs)
        return response


class UserService:
    @staticmethod
    def create_user(username, email, password, full_name, bio):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password, full_name=full_name, bio=bio)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def verify_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None
    
    
    @staticmethod
    def update_user(user_id, username, email, password, full_name, bio, linkedin_url, github_url):
        user = User.query.filter_by(user_id=user_id).first()

        if user:
           
            user.username = username
            user.email = email
            user.full_name = full_name
            user.bio = bio
        
            if linkedin_url and not linkedin_url.startswith("https://www.linkedin.com/"):
                return {"status": "error", "message": "Invalid LinkedIn URL"}, 400
            
            if github_url and not github_url.startswith("https://github.com/"):
                return {"status": "error", "message": "Invalid GitHub URL"}, 400

            user.linkedin_url = linkedin_url
            user.github_url = github_url

            db.session.commit()
            return user  


    @staticmethod
    def upload_image(file, user_id):
        # Check if the filename is empty
        if file.filename == '':
           return to_dict("error", "No file selected.")

        # Define allowed file extensions
        allowed_extensions = {'png', 'jpg', 'svg'}
        file_extension = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''

        # Check if the file extension is allowed
        if file_extension not in allowed_extensions:
            return to_dict("error", "File type not allowed.")

        # Generate a secure filename with a unique identifier
        unique_filename = f"{user_id}_{uuid.uuid4().hex}.{file_extension}"

        try:
            # Set Firebase storage bucket
            bucket = storage.bucket()
            blob = bucket.blob(f'user_images/{unique_filename}')

            # Upload the file directly to Firebase
            blob.upload_from_file(file, content_type=file.content_type)

            # Make the file publicly accessible
            blob.make_public()
            public_url = blob.public_url
            
            # Find the existing user by user_id
            existing_user = User.query.get(user_id)

            if existing_user:  # Check if user exists
                
                existing_user.image_filename = unique_filename
                existing_user.image_url = public_url
                existing_user.image_uploaded_at = datetime.utcnow()

                db.session.commit()  
            else:
                return to_dict("error", "User not found.")

        except Exception as e:
            print(f"An error occurred: {e}")  # Log the exception for debugging
            return to_dict("error", "An error occured")

        return to_dict("success", "Image uploaded successfully.", public_url=public_url)
    
    
    @staticmethod
    def add_user_links(user_id, linkedin_url, github_url):
        user = User.query.get(user_id)
        if not user:
            return {"status": "error", "message": "User not found"}, 404
        
        user.linkedin_url = linkedin_url
        user.github_url = github_url
        try:
            db.session.commit()
            return {"status": "success", "message": "External links added successfully"}, 200
        except Exception as e:
            db.session.rollback()  
            return {"status": "error", "message": str(e)}, 500
    

    
    @staticmethod
    def update_current_location(user_id, latitude, longitude):
        user = User.query.get(user_id)
        if user:
            user.current_location_latitude = latitude
            user.current_location_longitude = longitude
            db.session.commit()
            return user
        return None
    

    @staticmethod
    def get_current_location(user_id):
        user = User.query.get(user_id)
        if user:
            return {
                "current_location": {
                    "latitude": user.current_location_latitude,
                    "longitude": user.current_location_longitude,
                }
            }
        return None
        
        
    @staticmethod
    def update_live_location(user_id, latitude, longitude):
        user = User.query.get(user_id)
        if user:
            user.live_location_latitude = latitude
            user.live_location_longitude = longitude
            db.session.commit()
            return user
        return None
    
    @staticmethod
    def get_user_location(user_id):
        user = User.query.get(user_id)
        if user:
            return {
                "current_location": {
                    "latitude": user.current_location_latitude,
                    "longitude": user.current_location_longitude,
                },
                "live_location": {
                    "latitude": user.live_location_latitude,
                    "longitude": user.live_location_longitude,
                }
            }
        return None