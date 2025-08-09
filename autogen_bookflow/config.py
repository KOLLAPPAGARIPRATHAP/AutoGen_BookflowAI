# autogen_bookflow/config.py
"""import os
from dotenv import load_dotenv

#load_dotenv()

GROQ_API_KEY = "YOUR_API_KEY""

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it in your environment or a .env file.")

llm_config = {
    "config_list": [
        {
            "model": "llama3-8b-8192",
            "api_key": GROQ_API_KEY,
            "base_url": "https://api.groq.com/openai/v1",
        }
    ],
    "temperature": 0.3,
    "max_tokens": 1024,  # increased from 512
}
"""
import os
import streamlit as st

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it as a Streamlit secret or environment variable.")

llm_config = {
    "config_list": [
        {
            "model": "llama3-8b-8192",
            "api_key": GROQ_API_KEY,
            "base_url": "https://api.groq.com/openai/v1",
        }
    ],
    "temperature": 0.3,
    "max_tokens": 512,
}

#enhanced prompts for agents and runner 
''' #plot_agent
       backstory = (
        f"You are an expert story architect specializing in the {genre} genre. "
        "Given a user prompt describing a story idea, your task is to create a detailed, "
        "engaging, and coherent 3 to 5-point short plot outline. "
        "Each plot point should build logically on the previous ones and include key story elements such as "
        "conflict, character motivations, twists, and resolutions, while staying true to the {genre} style and tone. "
        "Focus on originality and maintaining suspense or emotional impact appropriate to the genre."
    )

  #scene_agent
     backstory = (
        f"You are a master storyteller who excels at crafting vivid, immersive scenes in the {genre} genre. "
        "Given a single plot point, you will expand it into a rich 200–300 word narrative scene. "
        "Your writing should paint strong visual imagery, evoke deep emotions, and immerse the reader in the atmosphere "
        "while maintaining a consistent genre style and tone. "
        "Include sensory details, character thoughts and feelings, and dynamic dialogue or action to bring the scene to life."
    )


 #runner
     initial_prompt = (
    f"You are collaborating agents working together to create a compelling {genre} story. "
    "First, PlotArchitect will develop a detailed 3 to 5-point plot outline based on the user's idea: "
    f"'{user_prompt}'. The outline should establish the setting, main conflict, character motivations, and key twists, "
    "structured clearly and engagingly. \n\n"
    "Once the plot outline is complete, SceneComposer will take each plot point sequentially and expand it into a vivid, "
    "immersive 200-300 word scene. Scenes should include rich sensory descriptions, emotional depth, and dialogue where appropriate, "
    "staying true to the genre's tone and style.\n\n"
    "Keep the conversation focused and collaborative, with each agent building on the other's output. "
    "Output the plot outline first, then the scenes in order, clearly labeling each section. "
    "End the entire response with the keyword 'TERMINATE' to indicate completion."
) '''




