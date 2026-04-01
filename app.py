import streamlit as st
# Import the compiled workflow from your agent.py file
from agents import app 

st.set_page_config(page_title="AI Developer Agent", page_icon="🤖", layout="wide")

st.title("🤖 Autonomous Code Agent")
st.markdown("This agent writes code, reviews it, generates tests, runs them in a secure E2B sandbox, and autonomously fixes any failures.")

# --- SIDEBAR: Display Graph Architecture ---
with st.sidebar:
    st.header("Architecture")
    st.markdown("Current LangGraph State Machine:")
    try:
        # Display the Mermaid graph we discussed earlier!
        png_bytes = app.get_graph().draw_mermaid_png()
        st.image(png_bytes, use_container_width=True)
    except Exception as e:
        st.warning("Graph visualization requires internet/dependencies to render.")

# --- MAIN UI: Input Area ---
default_prompt = "Write a Python function that takes a list of integers and a target value, and returns the two numbers that add up to the target."
requirement = st.text_area("What should the agent build?", value=default_prompt, height=100)

if st.button("Deploy Agent", type="primary"):
    if not requirement.strip():
        st.error("Please enter a requirement.")
    else:
        initial_state = {
            "requirement": requirement,
            "iterations": 0
        }

        # --- EXECUTION UI: Real-time Streaming ---
        st.write("### Agent Execution Log")
        
        # Use a status container to show it is "thinking"
        with st.status("Agent is working...", expanded=True) as status:
            
            final_summary = ""
            
            # app.stream() yields a dictionary containing the output of the node that just ran
            for output in app.stream(initial_state):
                
                # output.items() gets the node_name and the state updates it returned
                for node_name, state_update in output.items():
                    st.markdown(f"**✅ Completed Step:** `{node_name}`")

                    # Dynamically create expanders to show the exact output of each node
                    if node_name == "generate_code":
                        with st.expander("🔍 View Drafted Code"):
                            st.code(state_update.get("code", ""), language="python")
                            
                    elif node_name == "review_code":
                        with st.expander("📝 View Code Review"):
                            st.markdown(state_update.get("review_feedback", ""))
                            
                    elif node_name == "generate_test_cases":
                        with st.expander("🧪 View Generated Pytest Cases"):
                            st.code(state_update.get("test_cases", ""), language="python")
                            
                    elif node_name == "run_tests":
                        test_res = state_update.get("test_results", {})
                        passed = test_res.get("passed", False)
                        
                        if passed:
                            st.success("Sandbox Execution: All Tests Passed! 🎉")
                        else:
                            st.error("Sandbox Execution: Tests Failed! Routing back to code generation...")
                            
                        with st.expander("🖥️ View E2B Sandbox Terminal Logs"):
                            st.text(test_res.get("logs", "No logs available."))
                            
                    elif node_name == "analyze_failures":
                        with st.expander("🧠 View Failure Analysis"):
                            st.markdown(state_update.get("analysis", ""))
                            
                    elif node_name == "generate_summary":
                        # Save the summary to display prominently at the end
                        final_summary = state_update.get("summary", "")

            # Update the status box when the loop finishes
            status.update(label="Workflow Complete!", state="complete", expanded=False)

        # --- FINAL RESULTS ---
        st.divider()
        st.subheader("🎉 Final Report")
        if final_summary:
            st.markdown(final_summary)
        else:
            st.warning("The workflow ended without generating a summary.")