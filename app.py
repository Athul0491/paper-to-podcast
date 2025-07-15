import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from script import generate_script, parse_script_plan
from audio_gen import generate_podcast
from templates import enhance_prompt, initial_dialogue_prompt, plan_prompt

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI Clients
client = OpenAI(api_key=OPENAI_API_KEY)
llm = ChatOpenAI(model="gpt-4o-mini")

# Chains
chains = {
    "plan_script_chain": plan_prompt | llm | parse_script_plan,
    "initial_dialogue_chain": initial_dialogue_prompt | llm | StrOutputParser(),
    "enhance_chain": enhance_prompt | llm | StrOutputParser(),
}

# Set Streamlit page
st.set_page_config(page_title="🧠 Paper to Podcast", layout="centered")
st.title("🎙️ Paper to Podcast Wizard")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload your research paper (PDF)", type="pdf")

# Initialize session_state variables if not present
if "script" not in st.session_state:
    st.session_state.script = None
if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None
if "audio_generated" not in st.session_state:
    st.session_state.audio_generated = False
if "latest_mp3" not in st.session_state:
    st.session_state.latest_mp3 = None

# Save uploaded file
if uploaded_pdf:
    st.session_state.pdf_path = f"uploaded_{uploaded_pdf.name}"
    with open(st.session_state.pdf_path, "wb") as f:
        f.write(uploaded_pdf.getvalue())
    st.success("✅ PDF uploaded!")

# Generate Script
if st.session_state.pdf_path and st.button("🧠 Generate Podcast Script"):
    with st.spinner("Generating podcast script..."):
        script = generate_script(st.session_state.pdf_path, chains, llm)
        st.session_state.script = script
        st.session_state.audio_generated = False
    st.success("📜 Script ready!")

# Show script preview if available
if st.session_state.script:
    st.text_area("📜 Script Preview", st.session_state.script[:3000], height=300)

    # Generate Audio
    if st.button("🎧 Generate Audio"):
        with st.spinner("Generating podcast audio..."):
            generate_podcast(st.session_state.script, client)
            # Get latest mp3
            latest_mp3 = sorted([f for f in os.listdir() if f.endswith(".mp3")])[-1]
            st.session_state.latest_mp3 = latest_mp3
            st.session_state.audio_generated = True
        st.success("🎧 Podcast audio generated!")

# Show player + download
if st.session_state.audio_generated and st.session_state.latest_mp3:
    audio_bytes = open(st.session_state.latest_mp3, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")
    st.download_button("⬇️ Download Podcast", audio_bytes, file_name=st.session_state.latest_mp3)