# autogen_bookflow/config.py
"""import os
from dotenv import load_dotenv

# Load environment variables from a .env file
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
