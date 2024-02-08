from langchain_google_genai import GoogleGenerativeAIEmbeddings

def create_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    return embeddings


