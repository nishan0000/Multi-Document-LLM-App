from langchain.text_splitter import RecursiveCharacterTextSplitter


# Function to split all documents all together
def split_documents(pdf_documents, txt_documents, csv_documents):
    
    # Recursive character text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300, 
        chunk_overlap=60, 
        length_function=len
    )
    
    # Colelcting the splits for all documents combined
    splits = text_splitter.split_documents(pdf_documents + txt_documents + csv_documents)
    
    return splits
