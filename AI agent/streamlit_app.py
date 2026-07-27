import streamlit as st
from agent.travel_agent import executor
from utils.format import extract_output_text

st.set_page_config(page_title="AI Travel Agent", page_icon="🧳", layout="centered")

st.markdown(
    "<h1 style='text-align:center;'>🧳 AI Travel Agent</h1>"
    "<p style='text-align:center; color:gray;'>Plan trips with real weather, flights & hotel search</p>",
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = "streamlit-user"

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Where do you want to go?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Planning your trip..."):
            try:
                response = executor.invoke(
                    {"input": prompt},
                    config={"configurable": {"session_id": st.session_state.session_id}},
                )
                answer = extract_output_text(response["output"])
            except Exception as e:
                answer = f"Something went wrong: {e}"
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

with st.sidebar:
    st.header("About")
    st.write("Ask about destinations, weather, flights, and hotels. Chat history is saved in SQLite, so it persists across restarts.")
    if st.button("Clear chat (this session)"):
        st.session_state.messages = []
        st.rerun()
