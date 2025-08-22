from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def update_user_preferences(new_preferences: str, tool_context: ToolContext) -> dict:
    """Update the user's preferences in the session state.
    
    Args:
        new_preferences: The new preferences text to add
        tool_context: Context for accessing and updating session state
    
    Returns:
        A confirmation message
    """
    print(f"--- Tool: update_user_preferences called with '{new_preferences}' ---")
    
    # Get current preferences from state
    current_preferences = tool_context.state.get("user_preferences", "")
    
    # Add the new preferences
    updated_preferences = current_preferences + "\n" + new_preferences
    
    # Update state with the new preferences
    tool_context.state["user_preferences"] = updated_preferences
    
    return {
        "action": "update_user_preferences",
        "new_preferences": new_preferences,
        "message": f"Updated preferences: {new_preferences}",
    }


def update_user_name(new_name: str, tool_context: ToolContext) -> dict:
    """Update the user's name in the session state.
    
    Args:
        new_name: The new name for the user
        tool_context: Context for accessing and updating session state
    
    Returns:
        A confirmation message
    """
    print(f"--- Tool: update_user_name called with '{new_name}' ---")
    
    # Get current name from state
    old_name = tool_context.state.get("user_name", "")
    
    # Update the name in state
    tool_context.state["user_name"] = new_name
    
    return {
        "action": "update_user_name",
        "old_name": old_name,
        "new_name": new_name,
        "message": f"Updated user name from '{old_name}' to '{new_name}'",
    }


def get_current_state(tool_context: ToolContext) -> dict:
    """Get the current session state.
    
    Args:
        tool_context: Context for accessing session state
    
    Returns:
        The current state information
    """
    print("--- Tool: get_current_state called ---")
    
    return {
        "action": "get_current_state",
        "user_name": tool_context.state.get("user_name", "Unknown"),
        "user_preferences": tool_context.state.get("user_preferences", ""),
    }


# Create the root agent with tools
question_answering_agent = Agent(
    name="question_answering_agent",
    model="gemini-2.0-flash",
    description="Question answering agent with state management capabilities",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences and can update their information.
    
    The user's information is stored in state:
    - User's name: {user_name}
    - User preferences: {user_preferences}
    
    You can help users by:
    1. Answering questions about their preferences
    2. Updating their preferences when they provide new information
    3. Updating their name if needed
    4. Getting the current state information
    
    **IMPORTANT STATE UPDATE RULES:**
    
    When a user provides new information about themselves:
    1. **ALWAYS use the appropriate tool** to update the state
    2. **Don't just acknowledge verbally** - actually update the session state
    3. **Use update_user_preferences** for new likes, dislikes, or preferences
    4. **Use update_user_name** if they want to change their name
    5. **Use get_current_state** to check what's currently stored
    
    **Examples:**
    - If user says "I also like pizza" → use update_user_preferences("I also like pizza")
    - If user says "My name is John" → use update_user_name("John")
    - If user asks "What do you know about me?" → use get_current_state() first
    
    Always be friendly and helpful. When you update information, confirm what was updated.
    """,
    tools=[
        update_user_preferences,
        update_user_name,
        get_current_state,
    ],
)
