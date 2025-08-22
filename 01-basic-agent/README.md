# Basic ADK Agent Example

## What is an ADK Agent?
An **ADK Agent** (`LlmAgent`) is the "brain" of your app.  
It uses a Large Language Model (LLM) to:
- Understand natural language  
- Reason and make decisions  
- Generate responses  
- Use tools (if given)  
- Work with other agents  

Unlike fixed workflows, an `LlmAgent` is **dynamic** and decides what to do based on instructions and context.

---

## Project Structure
For ADK to run your agent, your folder must look like this:

```
parent_folder/
    agent_folder/
        __init__.py   # Imports agent.py
        agent.py      # Defines root_agent
        .env          # API key and environment settings
```

### Key Files
- **`__init__.py`** → must contain:  
  ```python
  from . import agent
  ```
- **`agent.py`** → must define:  
  ```python
  root_agent = ...
  ```
- Always run `adk` commands from the **parent folder**, not inside the agent folder.

---

## Agent Components
1. **Identity**
   - `name`: Unique ID of your agent  
   - `description`: Short summary (helps other agents know when to call it)  

2. **Model**
   - Example: `"gemini-2.0-flash"`  
   - Controls speed, cost, and capability  

3. **Instruction**
   - Defines what the agent should do, its personality, and rules  

4. **Tools (optional)**
   - Lets the agent fetch data, call APIs, or perform extra actions  

---

## Setup

### 1. Create a virtual environment
```bash
# macOS/Linux/Windows (Python 3.11 recommended)
python -m venv .venv
```

### 2. Activate the virtual environment
```bash
# macOS/Linux
source .venv/bin/activate

# Windows CMD
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Add your Google API key
- Rename `.env.example` → `.env`  
- Put your key under `GOOGLE_API_KEY`  

---

## Running the Agent
1. Go to the parent folder (e.g., `1-basic-agent/`)  
2. Start the web UI:
   ```bash
   adk web
   ```
3. Open the shown URL (default: `http://localhost:8000`)  
4. Pick your agent from the dropdown  
5. Start chatting!  

---

## Troubleshooting
If the agent doesn’t show up:
- Make sure you run `adk web` from the **parent folder**  
- Check `__init__.py` properly imports `agent`  
- Verify `agent.py` has `root_agent`  

---

## Other Run Options
- **Run in terminal:**  
  ```bash
  adk run [agent_name]
  ```
- **Start API server (FastAPI):**  
  ```bash
  adk api_server
  ```

---

## Example Prompts
Try these with your agent:
- "How do you say hello in Spanish?"  
- "What's a formal greeting in Japanese?"  
- "Tell me how to greet someone in French."  

Stop the server anytime with **Ctrl + C**.

---
