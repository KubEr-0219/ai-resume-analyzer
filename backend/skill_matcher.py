import re

SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "data science", "react", "javascript", "html", "css",
    "flask", "django", "nlp", "deep learning", "git"
]

def extract_skills(text):
    text = text.lower()
    extracted_skills = []

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            extracted_skills.append(skill)

    return list(set(extracted_skills))


def match_skills(resume_skills, job_role):
    job_roles = {
        "data scientist": ["python", "machine learning", "data science", "sql", "nlp"],
        "web developer": ["html", "css", "javascript", "react", "git"],
        "ai engineer": ["python", "deep learning", "nlp", "machine learning"]
    }

    required_skills = job_roles.get(job_role.lower(), [])
    matched = set(resume_skills).intersection(required_skills)

    match_percentage = int((len(matched) / len(required_skills)) * 100) if required_skills else 0

    return {
        "matched_skills": list(matched),
        "missing_skills": list(set(required_skills) - matched),
        "match_percentage": match_percentage
    }
