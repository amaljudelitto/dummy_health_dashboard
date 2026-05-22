import os
from google import genai
from dotenv import load_dotenv

# 1. Load the secure API key
load_dotenv()

# The new client automatically looks for the GEMINI_API_KEY environment variable
client = genai.Client()

def get_ai_wellness_insights(user_row):
    """
    Generates personalized wellness insights using the modern google-genai SDK.
    """
    user_context = f"""
    Age: {user_row['Age']}
    Lifestyle: {user_row['Lifestyle']}
    Primary Goal: {user_row['Wellness Goals']}
    Sleep: {user_row['Sleep Hours']} hours
    Stress Level: {user_row['Stress Level']}/10
    Activity Level: {user_row['Activity Level']}/10
    Water Intake: {user_row['Water Intake (L)']} Liters
    """

    system_instruction = """
    You are an analytical health AI assistant for AyurGenX. 
    Analyze the user's data and provide exactly 3 short, highly actionable lifestyle suggestions.
    Focus specifically on their 'Primary Goal'.
    Format the output as a simple markdown bulleted list. 
    """

    try:
        # 2. Use the new syntax to call the model
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_context,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
                max_output_tokens=150,
            )
        )
        return response.text
        
    except Exception as e:
        # Silent fallback
        print(f"API Error: {e}")
        return """
        * **🌙 Sleep Optimization:** Try to establish a consistent bedtime and avoid screens 1 hour before sleep.
        * **🧘 Stress Management:** Consider adding a 10-minute daily breathing or yoga routine.
        * **💧 Hydration Habit:** Keep a filled water bottle nearby to hit your daily intake.
        """