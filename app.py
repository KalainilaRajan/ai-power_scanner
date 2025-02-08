from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from celery import Celery
import openai
from utils import generate_interview_questions, analyze_emotional_intelligence, generate_job_recommendations
from werkzeug.utils import secure_filename

# Initialize app and extensions
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  # Ensure you have a DevelopmentConfig in config.py

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize JWT
jwt = JWTManager(app)
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

openai.api_key = app.config['OPENAI_API_KEY']

# Import models
from models import User, Resume

@app.route('/')
def login_page():
    return render_template('front.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.verify_password(data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/upload_resume', methods=['POST'])
@jwt_required()
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads/', filename)
        file.save(file_path)
        
        # Process the file (e.g., extract text from PDF/DOCX)
        resume_text = extract_text_from_file(file_path)
        
        new_resume = Resume(name=request.form['name'], email=request.form['email'], resume_text=resume_text)
        db.session.add(new_resume)
        db.session.commit()
        
        return jsonify({"message": "Resume uploaded successfully", "resume_id": new_resume.id})

    return jsonify({"message": "Invalid file type"}), 400

@app.route('/get_recommendations', methods=['GET'])
@jwt_required()
def get_recommendations():
    recommendations = generate_job_recommendations(current_user.id)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    # Create tables
    with app.app_context():
        db.create_all()  # Creates the tables defined in models.py

    app.run(debug=True)
