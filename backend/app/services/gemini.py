import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

def generate_recipe(ingredients: list[str], dietary_preferences: str = None, allergies: str = None) -> str:
    prompt = f"Create a recipe using the following ingredients: {", ".join(ingredients)}."
    if dietary_preferences:
        prompt += f" The recipe should be {dietary_preferences}."
    if allergies:
        prompt += f" The recipe should not contain {allergies}."
    
    prompt += " The recipe should have a title, a short description, a list of ingredients, and instructions."
    
    response = model.generate_content(prompt)
    return response.text
