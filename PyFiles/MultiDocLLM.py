import sys
sys.path.append('PyFiles')


import LLMConfigure
import MultiDocumentLoader
import DocumentSplitter
import CreateEmbeddings
import CreateRetriever
import CreateQAChain


def bot(data_folder_path, chain_type):
    
    llm = LLMConfigure.create_llm()

    pdf_documents, txt_documents, csv_documents = MultiDocumentLoader.load_all_documents(data_folder_path)

    splits = DocumentSplitter.split_documents(pdf_documents, txt_documents, csv_documents)

    embeddings = CreateEmbeddings.create_embeddings()

    retriever = CreateRetriever.create_retriever(embeddings, splits)

    qa = CreateQAChain.qa_chain(llm, retriever, chain_type)
    
    return qa





