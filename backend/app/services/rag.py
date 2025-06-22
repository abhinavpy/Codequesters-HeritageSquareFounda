import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from app.services.documents import get_retriever

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt_template = PromptTemplate.from_template(
    "System: You are an AI assistant. Answer the question based ONLY on the following context. If the context doesn't contain the answer, say you don't know.\nContext: {context}\nQuestion: {question}\nAnswer:"
)

def rag_chain(vector_store_path, question: str):
    """
    Builds and invokes a RAG chain using a direct Gemini integration.
    """
    # 1. Initialize the LLM directly from an environment variable
    # It will use the GEMINI_MODEL_NAME from your .env file, or default to "gemini-1.5-flash".
    model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-flash")
    llm = ChatGoogleGenerativeAI(model=model_name)

    # 2. Get the retriever for the specified vector store
    retriever = get_retriever(vector_store_path)

    # 3. Build the RAG chain using LangChain Expression Language (LCEL)
    # This is the modern, standard way to build chains in LangChain.
    rag_chain_pipeline = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )

    # 4. Invoke the chain with the user's question
    answer = rag_chain_pipeline.invoke(question)
    return answer