# autogen_bookflow/autogen_app.py

import streamlit as st
from story_runner import run_story_generation

# Streamlit Page Config
st.set_page_config(page_title="AutoGen Story Creator", layout="wide")
st.title("📖 AutoGen Story Creator")
st.markdown("Generate a short story outline and scene with AI agents powered by Groq & AutoGen.")

# Input
with st.form("story_form"):
    st.subheader("Step 1: Your Story Prompt")
    user_prompt = st.text_area("Enter your story idea:", height=150)

    st.subheader("Step 2: Choose Genre")
    genre = st.selectbox(
        "Select the story genre:",
        ["Mystery", "Romance", "Sci-Fi", "Fantasy", "Horror", "Inspirational"]
    )

    submit_btn = st.form_submit_button("Generate Story")

#Story Generation
if submit_btn:
    if not user_prompt.strip():
        st.error("⚠️ Please enter a story prompt.")
    else:
        with st.spinner("🤖 Generating plot outline and scene..."):
            plot_outline, scene_text = run_story_generation(user_prompt, genre)
            # Clean up scene text
            scene_text = scene_text.replace("TERMINATE", "").strip()

        st.success("✅ Story Generated!")
        st.subheader("📝 Plot Outline and 🎬 Scene")
        st.write(f"```\n{plot_outline}\n```")
        st.write(scene_text)
        

