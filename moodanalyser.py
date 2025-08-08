from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import tempfile

# Load environment variables from .env file
load_dotenv()


# Configure the Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


prompt = '''
You are a kind, emotionally-aware virtual companion for Nigerian mothers going through the postpartum period.

Your job is to chat with the mother in a way that:

Gently picks up on her emotional state (tired, happy, sad, frustrated, overwhelmed, etc.)

Offers real empathy, without sounding robotic or overly polished

Sprinkles in soft, familiar Nigerian expressions — e.g., “you dey try”, “small small”, “abeg”, “e no easy” — but never too much

Shares helpful, practical tips on caring for her baby and herself

Encourages her to speak freely, without judgement

Be real. Be gentle. Be helpful.

Don’t try to fix everything. It’s okay to just be present.
Don’t guess medical solutions. If she mentions something serious, gently recommend she speak to a healthcare professional.

Important: Don’t label her emotion directly (e.g., "You're sad.") — instead, reflect it in how you speak.

She should feel like she’s chatting with someone who gets it, not a therapist or a robot.
'''

st.set_page_config(page_title="Mum's Mind", page_icon="💕")
st.title("Mum's Mind. A space to be heard")
st.caption("We see you and hear you, mama mi!")



model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=prompt
)

def generate_check_in_question():
    """Asks the model to generate a single, proactive check-in question."""
    check_in_prompt = "Generate a single, warm, open-ended check-in question for a new Nigerian mother, in line with your persona. Just the question, nothing else."
    
    # Use generate_content for a single, non-chat turn
    response = model.generate_content(check_in_prompt)
    
    # Add the generated question to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})



# Initialize chat history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    generate_check_in_question()


# Initialize the chat object in session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])






# --- CHAT UI ---

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# Accept user input
if query := st.chat_input("Hello, Mum! How are you feeling today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    # Get the model's response from the ongoing chat session
    response = st.session_state.chat.send_message(query)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})

    st.session_state.show_check_in_button = True


# Show button only if last interaction is complete
if st.session_state.get("show_check_in_button", False):
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Check in on me ✨"):
            generate_check_in_question()
            
            st.session_state.show_check_in_button = False  

            st.rerun()

    