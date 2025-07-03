def get_retriever(vector_store, top_k: int = 4, search_type: str = "similarity"):
    """
    Creates a retriever from a FAISS vector store.

    Args:
        vector_store (FAISS): The FAISS vector store object
        top_k (int): Number of top similar documents to retrieve
        search_type (str): Type of search (default is "similarity")

    Returns:
        Retriever: A retriever object compatible with LangChain
    """
    retriever = vector_store.as_retriever(
        search_type=search_type,
        search_kwargs={"k": top_k}
    )
    return retriever
