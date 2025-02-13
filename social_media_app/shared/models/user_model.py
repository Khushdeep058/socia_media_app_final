from datetime import datetime
from shared.utils.db_utils import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    linkedin_url = db.Column(db.String(255)) 
    github_url = db.Column(db.String(255))
    image_filename = db.Column(db.String(255), nullable=True)
    image_uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    image_url = db.Column(db.String(255)) 
    current_location_latitude = db.Column(db.Float, nullable=True)
    current_location_longitude = db.Column(db.Float, nullable=True)
    live_location_latitude = db.Column(db.Float, nullable=True)
    live_location_longitude = db.Column(db.Float, nullable=True)

