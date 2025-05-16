from flask import Flask, request, render_template, jsonify, session
import uuid
import os
import json
from study_plan import generate_learning_advice
from advanced_prompting import create_few_shot_prompt
from prompt_generator import create_student_recommendation_prompt
from context_prompt import create_contextual_chat_prompt, enhance_conversation_history

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Stores conversation history and student profiles per session
conversation_histories = {}
student_profiles = {}

@app.route('/')
def index():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        conversation_histories[session['session_id']] = ""
        student_profiles[session['session_id']] = {}
    return render_template('index.html')

@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    topic = request.form.get("topic")
    if topic:
        # Minimal student data for now; expand as needed
        student_data = {"topic": topic}
        recommendation = generate_learning_advice(topic)

        session_id = session.get('session_id')
        if session_id:
            student_profiles[session_id] = student_data
            conversation_histories[session_id] = f"AI RECOMMENDATION:\n{recommendation}\n"

        return render_template("index.html", result=recommendation)
    return render_template("index.html", result="Please enter a topic.")

@app.route('/api/recommend', methods=['POST'])
def recommend():
    session_id = session.get('session_id', str(uuid.uuid4()))
    student_data = request.json
    prompt = create_few_shot_prompt(student_data)
    try:
        recommendation = generate_learning_advice(student_data)

        student_profiles[session_id] = student_data
        history = f"STUDENT PROFILE:\n{json.dumps(student_data, indent=2)}\n\nAI RECOMMENDATION:\n{recommendation}\n"
        conversation_histories[session_id] = history

        return jsonify({'success': True, 'recommendation': recommendation})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/chat', methods=['POST'])
def chat():
    session_id = session.get('session_id')
    if not session_id or session_id not in conversation_histories:
        return jsonify({'success': False, 'error': 'Session expired. Please refresh the page.'})

    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({'success': False, 'error': 'Empty message'})

    try:
        context = conversation_histories[session_id]
        student_profile = student_profiles.get(session_id, {})

        prompt = create_contextual_chat_prompt(user_message, student_profile, context)
        response = generate_learning_advice(prompt)

        conversation_histories[session_id] += f"\nUser: {user_message}\nAssistant: {response}\n"
        conversation_histories[session_id] = enhance_conversation_history(conversation_histories[session_id])

        return jsonify({'success': True, 'response': response})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/clear-chat', methods=['POST'])
def clear_chat():
    session_id = session.get('session_id')
    if not session_id or session_id not in conversation_histories:
        return jsonify({'success': False, 'error': 'Session not found'})
    try:
        conversation_histories[session_id] = ""
        student_profiles[session_id] = {}
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    os.makedirs("templates", exist_ok=True)
    print("Running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
