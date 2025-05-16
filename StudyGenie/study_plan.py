import json
import requests
from prompt_generator import create_student_recommendation_prompt

def get_llama_response(prompt):
    """Send a prompt to Ollama's Llama2 and get a response"""
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama2',
            'prompt': prompt,
            'stream': False,
            'temperature': 0.7,
            'top_p': 0.9,
            'max_tokens': 2048
        }
    )
    return response.json()['response']

def generate_learning_advice(topic_or_student_data):
    """Used by the Flask app to generate study plans or personalized advice."""
    # Flexible input: if it's a string, treat as topic; else, assume dict for recommendation
    if isinstance(topic_or_student_data, str):
        prompt = f"Provide a detailed study plan for the topic: {topic_or_student_data}"
    else:
        prompt = create_student_recommendation_prompt(topic_or_student_data)
    
    return get_llama_response(prompt)

# For testing the module directly
if __name__ == "__main__":
    student_example = {
        "grade": "9",
        "learning_style": "Visual",
        "academic_strengths": ["Mathematics", "Art"],
        "academic_challenges": ["Reading comprehension", "Note-taking"],
        "available_resources": ["Laptop", "Internet", "School library"],
        "study_preferences": ["Quiet environment", "Afternoon study sessions"]
    }

    print("Generating recommendation...\n")
    recommendation = generate_learning_advice(student_example)

    print("="*80)
    print("PERSONALIZED LEARNING RECOMMENDATION")
    print("="*80)
    print(recommendation)

    with open("recommendation_output.txt", "w") as f:
        f.write(recommendation)
    print("\nSaved to recommendation_output.txt")
