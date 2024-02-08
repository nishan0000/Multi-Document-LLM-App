from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import TextLoader



# Define a function to create a DirectoryLoader for a specific file type
def create_directory_loader(file_type, directory_path):
    
    # Define a dictionary to map file extensions to their respective loaders
    loaders = {
        '.pdf': PyPDFLoader,
        '.txt': TextLoader,
        '.csv': CSVLoader,
    }
    
    directory_loader = DirectoryLoader(
        path=directory_path,
        glob=f"**/*{file_type}",
        loader_cls=loaders[file_type],
    )
    
    return directory_loader


def load_all_documents(folder_path):
    
    # Create DirectoryLoader instances for each file type
    pdf_loader = create_directory_loader('.pdf', folder_path)
    txt_loader = create_directory_loader('.txt', folder_path)
    csv_loader = create_directory_loader('.csv', folder_path)
    
    # Load the files
    pdf_documents = pdf_loader.load()
    txt_documents = txt_loader.load()
    csv_documents = csv_loader.load()
    
    return pdf_documents, txt_documents, csv_documents


