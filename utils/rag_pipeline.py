from langchain_core.prompts import PromptTemplate
from langchain_cohere import ChatCohere  # or OpenAI, depending on your model
from langchain_core.documents import Document
from config.config import COHERE_API_KEY


llm = ChatCohere(model="command-r", temperature=0.3, cohere_api_key=COHERE_API_KEY)

def generate_answer(retriever, prompt: PromptTemplate, question: str):
    """
    Retrieves relevant docs, formats prompt, and gets LLM-generated answer.

    Args:
        retriever: Vector store retriever
        prompt_template (PromptTemplate): Prompt with input variables
        question (str): User question

    Returns:
        str: Generated answer
    """
    # Retrieve top documents
    retrieved_docs = retriever.invoke(question)
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # Step 2: Format the prompt
    filled_prompt = prompt.format(
        context=context_text,
        question=question
    )

    # Step 3: Invoke LLM
    response = llm.invoke(filled_prompt)

    return response