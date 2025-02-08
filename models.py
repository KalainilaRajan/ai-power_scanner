from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def verify_password(self, password):
        # Here you would compare the provided password with the hashed password
        return password == self.password_hash  # Simple check for demonstration, use hashing in real apps

# Resume model
class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    resume_text = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, default=0.0)
