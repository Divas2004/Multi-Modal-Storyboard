import google.generativeai as genai
import re

# 🔐 Configure Gemini
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-2.5-pro")

def generate_script(prompt):
    """Generates a 4-scene cinematic script using Gemini."""
    response = model.generate_content(
        f"""
You are a professional screenwriter. Break this story into 4 cinematic scenes.
Use this exact markdown format:

### **1. SCENE TITLE**

*   **Scene Description:** A few vivid lines describing the mood, setting, and scene dynamics.

*   **Character Actions:** A few bullet points describing what the main character(s) do.

Only return this markdown, no other introduction or conclusion.

Story: {prompt}
"""
    )
    return response.text.strip()

def extract_scenes(script_text):
    """Parses the script into scenes using regex for more flexibility."""
    scene_pattern = re.compile(
        r"### \*\*(\d+\.\s+.*?)\*\*\s*"
        r"\*+\s*\*\*Scene Description:\*\*\s*(.*?)\s*"
        r"\*+\s*\*\*Character Actions:\*\*",
        re.DOTALL
    )

    matches = scene_pattern.findall(script_text)
    scenes = []

    for title, desc in matches:
        scenes.append({
            "title": title.strip(),
            "desc": desc.strip().replace("\n", " ")
        })

    return scenes
