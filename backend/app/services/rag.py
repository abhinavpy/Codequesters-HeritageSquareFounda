from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.services.documents import get_retriever
from app.services.llm import ask_litellm

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt_template = PromptTemplate.from_template(
    "System: You are an AI assistant for Heritage Square. Answer the question based ONLY on the following context. If the context doesn't contain the answer, say you don't know.\nContext: {context}\nQuestion: {question}\nAnswer:"
)

def rag_chain(vector_store_path, question):
    retriever = get_retriever(vector_store_path)
    docs = retriever.get_relevant_documents(question)
    context = format_docs(docs)
    prompt = prompt_template.format(context=context, question=question)
    answer = ask_litellm(prompt)
    return answer