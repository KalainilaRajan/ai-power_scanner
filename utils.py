import openai

def generate_interview_questions(resume, job_description):
    prompt = f"Generate interview questions for a candidate with the following resume: {resume}. The job description is: {job_description}. Provide 5 questions."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text']

def analyze_emotional_intelligence(resume_text):
    prompt = f"Analyze the emotional intelligence of the following resume: {resume_text}. Provide a score between 0 and 100."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return float(response['choices'][0]['text'].strip())

def generate_job_recommendations(user_id):
    # This can be extended to fetch user data, jobs viewed or applied for
    prompt = f"Generate job recommendations for a user with these past interactions: User {user_id} has applied to roles in marketing and product management."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response['choices'][0]['text']
