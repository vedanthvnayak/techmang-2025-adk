# How It Works

1. The user provides a description of the email they need  
2. The LLM agent processes this request and generates both a subject and body  
3. The agent formats its response as a JSON object matching the `EmailContent` schema  
4. ADK validates the response against the schema before returning it  
5. The structured output is stored in the session state under the specified `output_key`  

---

# Important Limitations

When using `output_schema`:

- **No Tool Usage**: Agents with an output schema cannot use tools during their execution  
- **Direct JSON Response**: The LLM must produce a JSON response matching the schema as its final output  
- **Clear Instructions**: The agent's instructions must explicitly guide the LLM to produce properly formatted JSON  

---

# Project Structure

```
4-structured-outputs/
│
├── email_agent/                   # Email Generator Agent package
│   └── agent.py                   # Agent definition with output schema
│
└── README.md                      # This documentation
```

---

# Getting Started

## Setup

1. Create and activate a virtual environment from the root directory:

```bash
# macOS/Linux:
python3 -m venv .venv
source ../.venv/bin/activate

# Windows CMD:
python -m venv .venv
..\.venv\Scripts\activate.bat

# Windows PowerShell:
python -m venv .venv
..\.venv\Scripts\Activate.ps1
```

2. Create a `.env` file and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## Running the Example

```bash
cd 4-structured-outputs
adk web
```

Then select `email_generator` from the dropdown menu in the web UI.

---

# Example Interactions

Try these example prompts:

```
Write a professional email to my team about the upcoming project deadline that has been extended by two weeks.
```

```
Draft an email to a client explaining that we need additional information before we can proceed with their order.
```

```
Create an email to schedule a meeting with the marketing department to discuss the new product launch strategy.
```

---

# Key Concepts: Structured Data Exchange

Structured outputs are part of ADK's broader support for structured data exchange, which includes:

- **input_schema**: Define expected input format (not used in this example)  
- **output_schema**: Define required output format (used in this example)  
- **output_key**: Store the result in session state for use by other agents (used in this example)  

This pattern enables reliable data passing between agents and integration with external systems that expect consistent data formats.

---

# Additional Resources

- [ADK Structured Data Documentation](https://google.github.io/adk-docs/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key)
