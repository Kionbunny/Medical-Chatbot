
# Import necessary libraries and modules
from flask import Flask, render_template, jsonify, request  # Flask web framework
from src.helper import download_hugging_face_embeddings    # Custom helper for embeddings
from langchain_pinecone import Pinecone as PineconeVectorStore         # Pinecone vector store integration (langchain-pinecone==0.0.1)
from langchain_groq import ChatGroq                        # Groq chat model integration
from langchain.chains import create_retrieval_chain        # Retrieval chain for RAG
from langchain.chains.combine_documents import create_stuff_documents_chain # Combine docs
from langchain_core.prompts import ChatPromptTemplate      # Prompt template for LLM
from dotenv import load_dotenv                             # Load environment variables
from src.prompt import *                                   # Custom prompt(s)
import os



# Initialize Flask app
app = Flask(__name__)



# Load environment variables from .env file
load_dotenv()


# Retrieve API keys from environment
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

# Set API keys in environment (for libraries that read directly from os.environ)
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY



# Download or load the HuggingFace embeddings model
embeddings = download_hugging_face_embeddings()


# Pinecone index name for storing/retrieving embeddings
index_name = "rag-application" 

# Load the Pinecone vector store from an existing index
# (Assumes embeddings have already been upserted)

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)



# Create a retriever for semantic search (top 3 similar results)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Initialize the Groq chat model (free tier, high rate limits)
chatModel = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)

# Define the prompt template for the chat model
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),  # System prompt (instructions)
        ("human", "{input}"),      # User input placeholder
    ]
)

# Create the document QA chain (stuffing retrieved docs into prompt)
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)

# Create the Retrieval-Augmented Generation (RAG) chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)



# Route for the main chat page
@app.route("/")# default route to render the chat interface (chat.html)
def index():
    return render_template('chat.html')




# Route for handling chat messages (AJAX POST/GET)
@app.route("/get", methods=["GET", "POST"])
def chat():
    # Get user message from form
    msg = request.form["msg"]
    input = msg
    print(input)  # Debug: print user input

    # Pass user input to RAG chain and get response
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])  # Debug: print model response
    return str(response["answer"])




# Run the Flask app on all interfaces, port 8080, with debug mode enabled
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)