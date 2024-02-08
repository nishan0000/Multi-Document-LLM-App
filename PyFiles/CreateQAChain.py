from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory



def qa_chain(llm, retriever, chain_type):

    qa = RetrievalQA.from_chain_type(
        memory=ConversationBufferMemory(), 
        chain_type='stuff', 
        llm=llm, 
        retriever=retriever, 
        verbose=True
    )
    
    return qa
