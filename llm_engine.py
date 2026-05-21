import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_ai_wellness_insights(user_row):
    
    # Extract the raw data into a readable string
    user_context = f"""
    Age: {user_row['Age']}
    Lifestyle: {user_row['Lifestyle']}
    Primary Goal: {user_row['Wellness Goal']}
    Sleep: {user_row['Sleep Hours']} hours
    Stress Level: {user_row['Stress Level']}/10
    Activity Level: {user_row['Activity Level']}/10
    Water Intake: {user_row['Water Intake (L)']} Liters
    """

    # Engineer the System Prompt
    system_instruction = """
    You are an analytical health AI assistant for a project. 
    Analyze the user's data and provide exactly 3 short, highly actionable lifestyle suggestions.
    Focus specifically on their 'Primary Goal' and any metrics that seem unhealthy (e.g., high stress, low sleep).
    Format the output as a simple markdown bulleted list. 
    Do not give medical advice; explicitly state these are wellness suggestions.
    """

    # Call the Gemini API
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        
        response = model.generate_content(
            user_context,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=150,
            )
        )
        return response.text
        
    except Exception as e:
        return f"⚠️ AI Insight generation failed: {str(e)}. Please try again."