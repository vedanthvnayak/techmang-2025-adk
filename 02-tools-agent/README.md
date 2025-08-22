# Tool Agent Example

## What is a Tool Agent?
A **Tool Agent** is an ADK agent that can use tools to do more than just text responses.  
With tools, agents can:
- Search the web  
- Run code  
# Tool Agent Example

## What is a Tool Agent?
A **Tool Agent** is an ADK agent that can use tools to do more than just text responses.  
With tools, agents can:
- Search the web  
- Run code  
- Query your own data  
- Use custom functions  

This makes the agent more powerful and useful.

---

## Types of Tools

### 1. Built-in Tools
ADK provides ready-to-use tools:
- **Google Search** – search the web  
- **Code Execution** – run code snippets  
- **Vertex AI Search** – search your own data  

⚠️ **Limitations**:  
- You can only use **one built-in tool** per agent.  
- You **cannot** mix built-in tools with custom tools in the same agent.  

### 2. Custom Function Tools
You can write your own tools as Python functions.  

**Best Practices:**
- Use simple parameter types (string, int, list, dict)  
- No default values supported  
- Return a dictionary (best format):  
  ```python
  {"status": "success", "error_message": None, "result": "..."}
  ```
- The docstring of your function is sent to the LLM as the tool description  

---

## Limitations Recap
❌ Not supported examples:
```python
# Two built-in tools (not allowed)
tools=[built_in_code_execution, google_search]

# Built-in + custom function tool (not allowed)
tools=[google_search, get_current_time]
```

✅ To combine, use **multi-agent setup** instead.

---

## Implementation Example
The `agent.py` file defines:
1. Agent name + description  
2. Gemini model (e.g., `"gemini-2.0-flash"`)  
3. Instructions for how it should act  
4. Tools (e.g., `google_search`)  

It also has a commented-out custom tool (`get_current_time()`) you can enable for testing.

---

## Setup

### 1. Create and activate a virtual environment
```bash
# Create
python -m venv .venv

# macOS/Linux
source ../.venv/bin/activate

# Windows CMD
..\.venv\Scripts\activate.bat

# Windows PowerShell
..\.venv\Scripts\Activate.ps1
```

### 2. Add API Key
- Rename `.env.example` → `.env` in `tool_agent/`  
- Add your Google API key under `GOOGLE_API_KEY`

---

## Running the Agent
1. Go to the `2-tool-agent/` folder  
2. Start the web UI:
   ```bash
   adk web
   ```
3. Open the link shown in terminal (`http://localhost:8000`)  
4. Select **tool_agent** from dropdown  
5. Start chatting  

Other run options:
- Run in terminal:  
  ```bash
  adk run tool_agent
  ```
- Start API server:  
  ```bash
  adk api_server
  ```

---

## Example Prompts
- "Search for recent news about artificial intelligence"  
- "Find information about Google's Agent Development Kit"  
- "What are the latest advancements in quantum computing?"  

Stop the server anytime with **Ctrl + C**.

---

## Resources
- [Types of Tools](https://google.github.io/adk-docs/tools/#full-example-tavily-search)  
- [Function Tools Docs](https://google.github.io/adk-docs/tools/function-tools/)  
- [Built-in Tools Docs](https://google.github.io/adk-docs/tools/built-in-tools/)  
- Query your own data  
- Use custom functions  

This makes the agent more powerful and useful.

---

## Types of Tools

### 1. Built-in Tools
ADK provides ready-to-use tools:
- **Google Search** – search the web  
- **Code Execution** – run code snippets  
- **Vertex AI Search** – search your own data  

⚠️ **Limitations**:  
- You can only use **one built-in tool** per agent.  
- You **cannot** mix built-in tools with custom tools in the same agent.  

### 2. Custom Function Tools
You can write your own tools as Python functions.  

**Best Practices:**
- Use simple parameter types (string, int, list, dict)  
- No default values supported  
- Return a dictionary (best format):  
  ```python
  {"status": "success", "error_message": None, "result": "..."}
  ```
- The docstring of your function is sent to the LLM as the tool description  

---

## Limitations Recap
❌ Not supported examples:
```python
# Two built-in tools (not allowed)
tools=[built_in_code_execution, google_search]

# Built-in + custom function tool (not allowed)
tools=[google_search, get_current_time]
```

✅ To combine, use **multi-agent setup** instead.

---

## Implementation Example
The `agent.py` file defines:
1. Agent name + description  
2. Gemini model (e.g., `"gemini-2.0-flash"`)  
3. Instructions for how it should act  
4. Tools (e.g., `google_search`)  

It also has a commented-out custom tool (`get_current_time()`) you can enable for testing.

---

## Setup

### 1. Create and activate a virtual environment
```bash
# Create
python -m venv .venv

# macOS/Linux
source ../.venv/bin/activate

# Windows CMD
..\.venv\Scripts\activate.bat

# Windows PowerShell
..\.venv\Scripts\Activate.ps1
```

### 2. Add API Key
- Rename `.env.example` → `.env` in `tool_agent/`  
- Add your Google API key under `GOOGLE_API_KEY`

---

## Running the Agent
1. Go to the `2-tool-agent/` folder  
2. Start the web UI:
   ```bash
   adk web
   ```
3. Open the link shown in terminal (`http://localhost:8000`)  
4. Select **tool_agent** from dropdown  
5. Start chatting  

Other run options:
- Run in terminal:  
  ```bash
  adk run tool_agent
  ```
- Start API server:  
  ```bash
  adk api_server
  ```

---

## Example Prompts
- "Search for recent news about artificial intelligence"  
- "Find information about Google's Agent Development Kit"  
- "What are the latest advancements in quantum computing?"  

Stop the server anytime with **Ctrl + C**.

---

## Resources
- [Types of Tools](https://google.github.io/adk-docs/tools/#full-example-tavily-search)  
- [Function Tools Docs](https://google.github.io/adk-docs/tools/function-tools/) 
- [Built-in Tools Docs](https://google.github.io/adk-docs/tools/built-in-tools/)  
