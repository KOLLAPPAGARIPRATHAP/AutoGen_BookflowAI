# autogen_bookflow/agents/plot_architect.py

from autogen import AssistantAgent
from config import llm_config  # Import the new llm_config dictionary

def create_plot_architect(genre: str):
    """Returns a configured Plot Architect AutoGen agent."""
    
    backstory = (
        f"You are a master story planner specializing in the {genre} genre. "
        "Given a user prompt, you create a concise 3–5 short point plot outline "
        "that is engaging, coherent, and genre-appropriate."
    )
    
    plot_architect = AssistantAgent(
        name="PlotArchitect",
        llm_config=llm_config,  # Use the shared llm_config dictionary
        system_message=backstory
    )
    

    return plot_architect
