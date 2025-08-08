# autogen_bookflow/story_runner.py

from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from agents.plot_architect import create_plot_architect
from agents.scene_composer import create_scene_composer
from config import llm_config 

def run_story_generation(user_prompt: str, genre: str):
    """
    Orchestrates the AutoGen process.
    """

    #Create agents ---
    plot_architect = create_plot_architect(genre)
    scene_composer = create_scene_composer(genre)
    user_proxy = UserProxyAgent(
        name="User_Proxy",
        human_input_mode="NEVER",
        code_execution_config=False,
        llm_config=llm_config 
    )
    groupchat = GroupChat(
        agents=[user_proxy, plot_architect, scene_composer],
        messages=[],
        max_round=12,
        speaker_selection_method="round_robin"
    )
    manager = GroupChatManager(
        groupchat=groupchat, 
        llm_config=llm_config 
    )

    initial_prompt = (
    f"I need a story. First, as the PlotArchitect, create a 3–5 point short plot outline for a {genre} story "
    f"based on this idea: '{user_prompt}'. Once the outline is complete, "
    f"the SceneComposer should take the first plot point and write a 200-300 word scene. "
    f"Your final output must be the generated scene. End your response with 'TERMINATE'."
)

    
    chat_result = user_proxy.initiate_chat(
        manager,
        message=initial_prompt
    )
    
    final_message = chat_result.summary

    scene_text = final_message

    plot_outline = "Plot outline not found in the collaborative chat."
    for msg in chat_result.chat_history:
        if msg.get("name") == "PlotArchitect":
            plot_outline = msg.get("content")
            break

    return plot_outline, scene_text