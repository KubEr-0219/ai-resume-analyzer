from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills, match_skills

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file = request.files["resume"]
    job_role = request.form.get("job_role", "")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)
    result = match_skills(skills, job_role)

    return jsonify({
        "extracted_skills": skills,
        "analysis": result
    })


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
