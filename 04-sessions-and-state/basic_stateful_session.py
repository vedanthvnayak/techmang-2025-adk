import asyncio
import os
import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

# Load environment variables from the question_answering_agent directory
load_dotenv(os.path.join(os.path.dirname(__file__), "question_answering_agent", ".env"))


async def chat_with_agent():
    """Interactive chat interface with the agent."""
    # Create a new session service to store state
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name": "vedanth",
        "user_preferences": """
            I like to code.
            My favorite food is French.
            My favorite TV show is Game of Thrones.
            love to participate in HackersMang.
        """,
    }

    # Create a NEW session
    APP_NAME = "Vedanth Bot"
    USER_ID = "vedanth_user"
    SESSION_ID = str(uuid.uuid4())
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )
    print("🤖 Chat Session Started!")
    print(f"📝 Session ID: {SESSION_ID}")
    print(f"👤 User: {initial_state['user_name']}")
    print("\n" + "="*50)
    print("💬 Start chatting with your agent! (Type 'exit' to quit)")
    print("="*50 + "\n")

    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    # Chat loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check if user wants to exit
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Thanks for chatting! Session ended.")
                break
            
            if not user_input:
                continue

            # Create message for the agent
            new_message = types.Content(
                role="user", parts=[types.Part(text=user_input)]
            )

            print("\n🤖 Agent is thinking...\n")

            # Get agent response and track tool usage
            final_response = None
            tool_used = False
            
            for event in runner.run(
                user_id=USER_ID,
                session_id=SESSION_ID,
                new_message=new_message,
            ):
                # Check for tool usage
                if hasattr(event, 'content') and event.content and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, 'tool_response') and part.tool_response:
                            print(f"🔧 Tool used: {part.tool_response.output}")
                            tool_used = True
                
                if event.is_final_response():
                    if event.content and event.content.parts:
                        final_response = event.content.parts[0].text
                        print(f"🤖 Agent: {final_response}\n")
                        break

            if not final_response:
                print("🤖 Agent: Sorry, I couldn't generate a response. Please try again.\n")

            # Display current session state after each interaction
            print("-" * 40)
            session = await session_service_stateful.get_session(
                app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
            )
            print("📊 Current Session State:")
            for key, value in session.state.items():
                if key == "user_preferences":
                    print(f"  {key}: {value.strip()}")
                else:
                    print(f"  {key}: {value}")
            print("-" * 40 + "\n")

        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'exit' to quit.\n")


async def main():
    """Main function to run the chat interface."""
    await chat_with_agent()


if __name__ == "__main__":
    asyncio.run(main())