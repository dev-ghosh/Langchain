from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
#LLM
llm = ChatGroq(model="llama-3.1-8b-instant")
# Embeddings (HuggingFace - local & free)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def create_vector_db_frm_yt_url(video_url:str)-> FAISS:
    loader=YoutubeLoader.from_youtube_url(video_url)
    transcript=loader.load()

    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    docs=text_splitter.split_documents(transcript)

    db=FAISS.from_documents(docs,embeddings)
    return db

def get_response_from_query(db,query,k=2):
    docs=db.similarity_search(query,k=k)
    docs_page_content=" ".join([d.page_content for d in docs])

    llm=ChatGroq(model="llama-3.1-8b-instant")

    prompt=PromptTemplate(
        input_variables=["questions","docs"],
        template="""
        You are a helpful YouTube assistant.

        Use ONLY the transcript context below to answer the question in short.
        If the answer is not in the transcript, say "I don't know."

        Transcript:
        {docs}

        Question:
        {questions}

        Answer:
        """
    )

    chain= prompt | llm
    response=chain.invoke({"questions": query, "docs": docs_page_content})
    return response.content.strip() # strip removes extra spaces at beg/end