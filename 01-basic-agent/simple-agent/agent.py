from google.adk.agents import Agent

root_agent = Agent(
    name="simple_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash", #gemini-2.0-flash-live-001
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
