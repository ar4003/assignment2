"""
JobYaari AI Chatbot - Simplified Version with better formatting & flexible search
"""

import os
import json
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'secret')

class JobYaariChatbotSimple:
    def __init__(self):
        self.kb_path = 'training_data/knowledge_base.json'
        self.load_kb()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        logger.info(f"Chatbot initialized with {self.kb['metadata']['total_jobs']} jobs")

    def load_kb(self):
        with open(self.kb_path, 'r', encoding='utf-8') as f:
            self.kb = json.load(f)

    def get_quick_stats(self):
        return {"total_jobs": self.kb['metadata']['total_jobs']}

    def search_jobs(self, query, category=None):
        q = query.lower()
        if category:
            return self.kb['categories'].get(category, [])[:15]
        results = []
        for cat, job_list in self.kb['categories'].items():
            for job in job_list:
                text = f"{job['job_title']} {job['organization']} {job['qualification']}".lower()
                if any(tok in text for tok in q.split()):
                    results.append(job)
        return results[:15]

    def format_jobs(self, jobs, q):
        if not jobs:
            return f"No jobs found for '{q}'."
        resp = f"Here are some {q}:\n\n"
        for i, j in enumerate(jobs[:5], 1):
            resp += (f"{i}. **{j['job_title']}** at _{j['organization']}_\n"
                     f"   - Salary: {j['salary']}\n"
                     f"   - Experience: {j['experience']}\n"
                     f"   - Qualification: {j['qualification']}\n"
                     f"   - Location: {j['location']}\n"
                     f"   - Vacancies: {j['vacancies']}\n\n")
        return resp.strip()

    def get_response(self, msg):
        low = msg.lower()
        for c in ['engineering', 'science', 'commerce', 'education']:
            if c in low:
                jobs = self.search_jobs(msg, category=c)
                return self.format_jobs(jobs, f"{c.title()} jobs")
        jobs = self.search_jobs(msg)
        return self.format_jobs(jobs, msg)

bot = JobYaariChatbotSimple()

@app.route('/')
def home():
    stats = bot.get_quick_stats()
    return render_template('index.html', stats=stats)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get('message', '').strip()
    if not msg:
        return jsonify(response="Please ask about government jobs.")
    reply = bot.get_response(msg)
    return jsonify(response=reply)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
