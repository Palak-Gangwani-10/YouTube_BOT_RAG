from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from config.config import COHERE_API_KEY
# 
def split_text_into_chunks(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[Document]:
    """
    Splits plain text into chunks using LangChain's RecursiveCharacterTextSplitter.

    Args:
        text (str): The full text to split
        chunk_size (int): Size of each chunk in characters
        chunk_overlap (int): Overlap between chunks in characters

    Returns:
        List[Document]: A list of LangChain Document objects
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.create_documents([text])
    return chunks

def create_vector_store_from_chunks(chunks, model_name="embed-english-v3.0"):
    """
    Generates embeddings for text chunks using Cohere and stores them in a FAISS vector store.

    Args:
        chunks (List[Document]): A list of LangChain Document objects
        model_name (str): Cohere model to use for embedding

    Returns:
        FAISS: A LangChain-compatible FAISS vector store
    """
    embeddings = CohereEmbeddings(cohere_api_key=COHERE_API_KEY, model=model_name)
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store