import streamlit as st
from utils.api_helpers import fetch_transcript
from utils.embedding_utils import split_text_into_chunks, create_vector_store_from_chunks
from utils.prompt_templates import get_transcript_qa_prompt
from utils.retriever_utils import get_retriever
from utils.rag_pipeline import generate_answer

# Set page config
st.set_page_config(
    page_title="YouTube Bot",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title of the app
st.title("🎥 YouTube Bot")

# Input fields
video_id = st.text_input("Enter YouTube Video ID", placeholder="e.g., dQw4w9WgXcQ")
question = st.text_input("Enter your question about the video", placeholder="What is the main topic discussed in this video?")

# Submit button
if st.button("Get Answer"):
    if video_id and question:
        try:
            with st.spinner("Processing your request..."):
                # Get transcript and process
                transcript = fetch_transcript(video_id)
                chunks = split_text_into_chunks(transcript)
                vector_store = create_vector_store_from_chunks(chunks)
                retriever = get_retriever(vector_store, top_k=4, search_type="similarity")
                prompt = get_transcript_qa_prompt()
                response = generate_answer(retriever, prompt, question)
                
                # Create a container for the response
                response_container = st.container()
                with response_container:
                    st.markdown("### Answer")
                    # Split the content by newlines and display each paragraph
                    paragraphs = response.content.split('\n\n')
                    for paragraph in paragraphs:
                        if paragraph.strip():  # Only display non-empty paragraphs
                            st.markdown(f"{paragraph.strip()}")
                            st.markdown("---")  # Add a separator between paragraphs
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter both a video ID and a question.") 