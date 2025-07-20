# app.py
import streamlit as st
from utils.script_generator import generate_script, extract_scenes
from utils.storyboard_generator import generate_storyboard
from utils.video_generator import generate_video
import tempfile
import time

st.set_page_config(page_title="🎬 Storyboard & Video Generator", layout="centered")
st.title("🎥 Multi-Modal Storyboard & Video Scene Generator")

prompt = st.text_area("📜 Enter your story idea:", placeholder="A detective discovers a clue in a rainy city at night.")

if st.button("🚀 Generate Full Script, Storyboards, and Video Clips"):
    if not prompt.strip():
        st.warning("Please enter a story prompt.")
    else:
        progress = st.progress(0, text="Starting generation...")

        # 1. Generate script
        with st.spinner("✍️ Generating cinematic script..."):
            script_text = generate_script(prompt)
            scenes = extract_scenes(script_text)
        progress.progress(0.1, text="✅ Script parsed into scenes")

        if not scenes:
            st.error("❌ No scenes parsed. Try a more detailed prompt.")
        else:
            st.success("✅ Script generation complete!")

            # 2. Display Script
            st.header("📘 Full Script")
            for i, scene in enumerate(scenes):
                st.markdown(f"### 🎬 Scene {i+1}: {scene['title']}")
                st.markdown(f"📝 **Scene Description:**\n{scene['desc']}", unsafe_allow_html=True)
            progress.progress(0.25, text="📘 Script displayed")

            # 3. Generate Storyboards
            st.header("🎨 Storyboard Images")
            images = []
            for i, scene in enumerate(scenes):
                with st.spinner(f"🖼️ Generating storyboard for Scene {i+1}..."):
                    image = generate_storyboard(scene["desc"])
                    images.append(image)
                    st.image(image, caption=f"Scene {i+1}: {scene['title']}", width=400)
                    progress.progress(0.25 + (i + 1) * 0.1, text=f"🎨 Storyboard {i+1}/4 generated")

            # 4. Generate Videos
            st.header("🎞️ Video Clips")
            for i, image in enumerate(images):
                with st.spinner(f"🎬 Generating video clip for Scene {i+1}..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmpfile:
                        generate_video(image, tmpfile.name)
                        st.video(tmpfile.name, format="video/mp4")
                        progress.progress(0.65 + (i + 1) * 0.08, text=f"🎞️ Video {i+1}/4 generated")

            progress.progress(1.0, text="✅ All scenes completed and displayed!")
            st.balloons()
