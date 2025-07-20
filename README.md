# 🎬 Multi-Modal Storyboard & Video Scene Generator

This Streamlit app takes a text prompt as input and generates a **4-scene cinematic experience** that includes:
- A structured script (scene descriptions and character actions)
- A storyboard image for each scene (via Stable Diffusion)
- A short video clip for each scene (via Stable Video Diffusion)

---

## ✨ Features
- Uses **Gemini Pro** to generate 4-scene script from your story prompt.
- Generates high-quality storyboard images.
- Converts storyboards into short cinematic video clips.
- Fully interactive via a Streamlit web interface.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-modal-storyboard.git
cd multi-modal-storyboard

### 2. Create and activate Virtual Environment

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add Your Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")


Usage:

Run the app locally:

streamlit run app.py

You'll get a UI to:
Enter a prompt
View the generated script
See storyboards and video clips for all 4 scenes
