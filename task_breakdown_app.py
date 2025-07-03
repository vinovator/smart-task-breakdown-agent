import streamlit as st
from task_breakdown_agent import breakdown_goal_with_memory
from utils import load_memory

st.set_page_config(page_title="AI Task Breakdown Agent", layout="wide")  
st.title("AI Task Breakdown Agent")  

goal_input = st.text_area("Enter your goal here:", height=100)

if st.button("Breakdown Goal"):
    with st.spinner("Breaking down your goal..."):
        result = breakdown_goal_with_memory(goal_input)
        st.success("Goal breakdown completed!")
        st.markdown(result)

st.markdown("---")
st.markdown("### Memory of Past Tasks")

memory = load_memory()
for entry in reversed(memory[-5:]):
    st.markdown(f"**Goal:** {entry['goal']}")
    st.markdown(f"**Tasks:** {entry['tasks']}")
    st.markdown(f"**Timestamp:** {entry['timestamp']}")
    st.markdown("---")

    