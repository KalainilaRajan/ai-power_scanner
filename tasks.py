from app import celery
from models import Resume
from utils import analyze_emotional_intelligence, generate_interview_questions
from app import db

@celery.task
def process_resume(resume_id):
    resume = Resume.query.get(resume_id)
    if not resume:
        return "Resume not found"
    
    # Emotional Intelligence Analysis
    emotional_intelligence_score = analyze_emotional_intelligence(resume.resume_text)
    resume.emotional_intelligence = emotional_intelligence_score

    # Generate Interview Questions
    job_description = "Sample job description for software engineer"
    interview_questions = generate_interview_questions(resume.resume_text, job_description)
    
    # Save results
    resume.score = emotional_intelligence_score
    db.session.commit()

    return f"Processed resume {resume.id}, Emotional Intelligence Score: {emotional_intelligence_score}"

@celery.task
def check_compliance(resume_id):
    resume = Resume.query.get(resume_id)
    # Check for legal compliance (e.g., discriminatory language)
    # This can be integrated with OpenAI API or a custom compliance model
    compliance_issues = []  # Placeholder for actual logic
    return compliance_issues
