"""Streamlit UI for exploring the agentic design pattern examples."""

import streamlit as st


st.set_page_config(
    page_title="Agentic Design Patterns",
    page_icon="🤖",
    layout="wide",
)


def run_tool_using(question: str) -> dict:
    from patterns.tool_using.graph import build_graph

    return build_graph().invoke({"question": question})


def run_planner_executor(task: str) -> dict:
    from patterns.planner_executor.graph import build_graph

    return build_graph().invoke({"task": task})


st.title("Agentic Design Patterns")
st.caption("Explore how different agent workflows solve tasks.")

pattern = st.sidebar.radio(
    "Choose a design pattern",
    ("Tool-using agent", "Planner–executor"),
)

if pattern == "Tool-using agent":
    st.header("Tool-using agent")
    st.write(
        "The reasoning agent turns a natural-language math question into an "
        "expression, then hands it to the calculator tool."
    )
    with st.form("tool_using_form"):
        question = st.text_input(
            "Math question",
            placeholder="What is the square of the average of 10 and 5?",
        )
        submitted = st.form_submit_button("Run tool-using agent", type="primary")

    if submitted:
        if not question.strip():
            st.warning("Enter a math question to run this pattern.")
        else:
            try:
                with st.spinner("The agent is reasoning and using the calculator…"):
                    result = run_tool_using(question.strip())
                st.subheader("Workflow results")
                first, second = st.columns(2)
                first.metric("Generated expression", result.get("expression", ""))
                second.metric("Calculator result", result.get("result", ""))
                with st.expander("See the workflow state"):
                    st.json(result)
            except Exception as exc:
                st.error(f"The tool-using workflow could not complete: {exc}")

else:
    st.header("Planner–executor")
    st.write(
        "The planner breaks a task into up to three steps. The executor then "
        "works through each step and combines its responses."
    )
    with st.form("planner_executor_form"):
        task = st.text_area(
            "Task",
            placeholder="Create a launch plan for an AI chatbot product.",
            height=120,
        )
        submitted = st.form_submit_button("Plan and execute", type="primary")

    if submitted:
        if not task.strip():
            st.warning("Enter a task to run this pattern.")
        else:
            try:
                with st.spinner("The planner and executor are working…"):
                    result = run_planner_executor(task.strip())
                st.subheader("Plan")
                plan = result.get("plan", [])
                if plan:
                    for step in plan:
                        cleaned_step = step.strip().removeprefix("-").strip()
                        if cleaned_step:
                            st.markdown(f"- {cleaned_step}")
                else:
                    st.info("The planner did not return any steps.")
                st.subheader("Execution")
                st.markdown(result.get("output", "No execution output was returned."))
                with st.expander("See the workflow state"):
                    st.json(result)
            except Exception as exc:
                st.error(f"The planner–executor workflow could not complete: {exc}")

st.sidebar.divider()
st.sidebar.caption("An OpenAI API key is required to run the workflows.")
