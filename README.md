# Agentic Design Patterns

This project demonstrates agentic AI design patterns implemented with
LangGraph. It currently includes a tool-using agent and a planner–executor
workflow, with a Streamlit interface for trying both interactively.

## Requirements

- Python 3.10 or newer
- An OpenAI API key

## Setup

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Set `OPENAI_API_KEY` in your shell, or add it to a `.env` file in the project
root:

```text
OPENAI_API_KEY=your-api-key
```

## Run the Streamlit app

From the project root, run:

```bash
streamlit run app.py
```

Choose a pattern in the sidebar, enter a question or task, and submit it to see
the workflow results. The app displays the expression and calculator result for
the tool-using pattern, and the generated plan and execution output for the
planner–executor pattern. Expand **See the workflow state** to inspect the full
state returned by LangGraph.

## Included patterns

### Tool-using agent

The reasoning agent translates a natural-language math question into a Python
math expression. The graph passes that expression to the calculator tool and
returns the result.

### Planner–executor

The planner creates a plan of up to three steps for a task. The executor
processes each step and combines the responses into one output.

## Running the backend examples

The original command-line examples are also available:

```bash
python -m patterns.tool_using.run
python -m patterns.planner_executor.run
```
