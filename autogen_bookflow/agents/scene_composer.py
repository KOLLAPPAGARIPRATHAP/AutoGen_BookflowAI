# autogen_bookflow/agents/scene_composer.py

from autogen import AssistantAgent
from config import llm_config # Import the new llm_config dictionary

def create_scene_composer(genre: str):
    """Returns a configured Scene Composer AutoGen agent."""
    
    backstory = (
        f"You are a skilled storyteller specializing in vivid, immersive {genre} scenes. "
        "You take a single plot point and expand it into a 200–300 word scene "
        "with strong imagery, emotional engagement, and genre-consistent style."
    )
    
    scene_composer = AssistantAgent(
        name="SceneComposer",
        llm_config=llm_config, # config llm
        system_message=backstory
    )
    

    return scene_composer
