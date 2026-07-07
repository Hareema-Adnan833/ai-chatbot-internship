import streamlit as st
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="auto",
    api_key=hf_token,
)
st.set_page_config(page_title="Database AI Chatbot", page_icon="🤖")

st.title("🤖 Database AI Chatbot")
st.write("Ask me anything related to Databases, SQL, MySQL, PostgreSQL, MongoDB, etc.")

# ====================================
# Prompt Engineering Sidebar
# ====================================

st.sidebar.title("🧠 Prompt Engineering")

technique = st.sidebar.selectbox(
    "Choose Prompting Technique",
    (
        "Zero-Shot",
        "One-Shot",
        "Few-Shot",
        "Role-Based",
        "Intrusion Detection"
    )
)

st.sidebar.markdown("---")

st.sidebar.subheader("⚙️ Response Settings")

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.5,
    value=0.7,
    step=0.1
)

response_length = st.sidebar.selectbox(
    "Response Length",
    ["Short", "Medium", "Detailed"]
)

difficulty = st.sidebar.selectbox(
    "Explanation Level",
    ["Beginner", "Intermediate", "Advanced"]
)

include_example = st.sidebar.checkbox("Include Real-life Example")

clear_chat = st.sidebar.button("🗑 Clear Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

if clear_chat:
    st.session_state.messages = []
    st.rerun()    

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your question here...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

# ====================================
# Prompt Engineering Logic
# ====================================

    if technique == "Zero-Shot":

        system_prompt = """
        You are a helpful database assistant.
        Answer only database related questions.
        """

    elif technique == "One-Shot":

        system_prompt = """
        You are a database assistant.

        Example:

        User: What is SQL?

        Assistant:
        SQL is used to communicate with databases.

        Answer the next question similarly.
        """

    elif technique == "Few-Shot":

        system_prompt = """
        You are a database assistant.

        Examples:

        User: What is SQL?

        Assistant:
        SQL is a language for databases.

        User: What is Primary Key?

        Assistant:
        A Primary Key uniquely identifies every record.

        User: What is Normalization?

        Assistant:
        It reduces redundancy.

        Continue answering in the same style.
        """

    elif technique == "Role-Based":

        system_prompt = """
        You are an experienced Database Professor.

        Explain everything:
        - In simple English
        - Give examples
        - Use bullet points
        """

    else:

        system_prompt = """
        You are a secure database assistant.

        Only answer database questions.

        If a question is outside databases,
        politely refuse.
        """

    system_prompt += f"""

    Response Length: {response_length}

    Explanation Level: {difficulty}

    """

    if include_example:
      system_prompt += "\nAlways include one real-life database example."        

    try:
        completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        max_tokens=500,
        temperature=temperature,
        )

        assistant_message = completion.choices[0].message.content

        st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
        )

        with st.chat_message("assistant"):
            st.markdown(assistant_message)

    except Exception as e:
        st.error(f"❌ Error: {e}")

