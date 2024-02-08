from langchain.vectorstores import Chroma


def create_retriever(embeddings, splits):
    # Creating vector database
    db = Chroma.from_documents(documents=splits, embedding=embeddings)
    
    # Create retriever form db
    retriever = db.as_retriever()
    
    return retriever

