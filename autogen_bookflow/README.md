

📖 AutoGen BookFlow – Short Story Creator
AutoGen BookFlow is a Streamlit app that uses AutoGen’s multi-agent system with Groq’s LLaMA 3 model to turn your story ideas into narratives by:
Creating a 3–5 point plot outline from your prompt
Writing a 200–300 word scene based on the first plot point

🚀 Features
Two AutoGen agents:
• Plot Architect — crafts plot outlines
• Scene Composer — writes vivid scenes
Genre selection to customize style
Powered by Groq LLM with langchain_groq.ChatGroq
Easy-to-use Streamlit interface
Modular and extendable codebase

## 📂 Project Structure
autogen_bookflow/
│
├── init.py
├── config.py # Groq LLM setup with ChatGroq
├── agents/
│ ├── plot_architect.py 
│ ├── scene_composer.py 
├── story_runner.py 
├── autogen_app.py 
├── requirements.txt
├── README.md