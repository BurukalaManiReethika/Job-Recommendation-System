from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

app = Flask(__name__)

# Load jobs data
jobs = pd.read_csv("jobs.csv")

# Convert text to vectors
vectorizer = TfidfVectorizer()
job_vectors = vectorizer.fit_transform(jobs['skills'])

# Function to extract text from PDF
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route('/recommend', methods=['POST'])
def recommend():
    file = request.files['resume']
    
    resume_text = extract_text(file)
    
    resume_vector = vectorizer.transform([resume_text])
    
    similarity = cosine_similarity(resume_vector, job_vectors)
    
    jobs['score'] = similarity[0]
    
    top_jobs = jobs.sort_values(by='score', ascending=False).head(3)
    
    return jsonify(top_jobs.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
