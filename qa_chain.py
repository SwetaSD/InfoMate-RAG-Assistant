from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def build_qa_chain(vector_store, k=3):
    retriever = vector_store.as_retriever(search_kwargs={"k": k})

    prompt = PromptTemplate.from_template(
        """You are a helpful assistant.
Answer ONLY using the given context.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:"""
    )

    llm = ChatOllama(
        model="phi3:mini",
        temperature=0
    )

    chain = (
        {
            # 🔹 retriever gets ONLY the question string
            "context": lambda x: retriever.invoke(x["question"]),
            "question": lambda x: x["question"]
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
