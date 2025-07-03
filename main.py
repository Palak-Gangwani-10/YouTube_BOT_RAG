from utils.api_helpers import fetch_transcript
from utils.embedding_utils import split_text_into_chunks, create_vector_store_from_chunks
from utils.prompt_templates import get_transcript_qa_prompt
from utils.retriever_utils import get_retriever
from utils.rag_pipeline import generate_answer

video_id = "Gfr50f6ZBvo"
question = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"

try:
    transcript = fetch_transcript(video_id)
    chunks = split_text_into_chunks(transcript)
    vector_store = create_vector_store_from_chunks(chunks)
    retriever = get_retriever(vector_store, top_k=4, search_type="similarity")
    prompt = get_transcript_qa_prompt()
    response = generate_answer(retriever, prompt, question)
    print(response)
except Exception as e:
    print(f"Error: {e}")
