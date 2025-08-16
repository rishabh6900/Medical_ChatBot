from flask import Flask,render_template,jsonify,request
from src.helper import download_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

# load_dotenv()

# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
# os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# embedding=download_embedding()


@app.route("/")
def index():
    return render_template("index5.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
