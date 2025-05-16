def create_few_shot_prompt(student_data):
    """Create a prompt with examples to guide the model's responses"""
    from prompt_engineering import create_student_recommendation_prompt
    
    # Generate the prompt for the current student profile without 'available_resources'
    # Assuming create_student_recommendation_prompt excludes 'available_resources' now
    base_prompt = create_student_recommendation_prompt(student_data)
    
    # Few-shot example with "Available Resources" removed
    examples = """
EXAMPLE STUDENT PROFILES AND HIGH-QUALITY RECOMMENDATIONS:

EXAMPLE 1:
Student Profile:
- Grade Level: 8
- Learning Style: Visual
- Academic Strengths: Art, Science
- Academic Challenges: Mathematics, Organization
- Study Preferences: Short study sessions, Afternoon

Recommendation:
1. LEARNING APPROACH:
   • Use color-coded math notes with visual representations of concepts
   • Create mind maps for organizing scientific concepts
   • Break study sessions into 25-minute intervals with 5-minute breaks
   • Use visual timers to track study sessions

2. RESOURCE RECOMMENDATIONS:
   • GeoGebra app (works offline) for visual math practice
   • Khan Academy videos (download when internet available)
   • Quizlet for flashcards with visual elements
   • Microsoft OneNote for visual organization of notes

NOW PLEASE PROVIDE A RECOMMENDATION FOR THE NEW STUDENT:
"""
    
    # Return examples + base prompt (without available resources)
    return examples + "\n" + base_prompt
