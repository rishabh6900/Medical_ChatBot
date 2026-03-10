# Medical_ChatBot using Langchain,Gemini
An AI-powered Medical Chatbot that answers healthcare-related questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

The chatbot retrieves relevant medical information from a vector database and generates accurate responses using an LLM.


##  Features

1. **AI-powered Medical Q&A System**
2. **Retrieval-Augmented Generation (RAG)** for context-aware answers
3. **PDF Document Processing** for medical knowledge ingestion
4. **Semantic Search** using vector embeddings
5. **Pinecone Vector Database** for fast similarity search
6. **Flask Web Interface** for interactive chatbot experience
7. **LLM-powered Response Generation**
8. **LangSmith Integration** for tracing, debugging, and monitoring LLM pipelines

## How to run  

### step-1 
```bash
git clone https://github.com/rishabh6900/Medical_ChatBot 
```

### step-2 
```bash
cd Medical_ChatBot 
```
### step-3  
```bash
conda create -n medibot python=3.10 -y
```
### step-4  
```bash 
conda create -n MC python=3.10.18 -y
```
### step-5
```bash
conda activate MC
``` 
### step-6
```bash
pip install -r requirements.txt
```
### step-7
Create .env file 
```bash
GOOGLE_API_KEY = "AIzaSybw"
LANGCHAIN_API_KEY= "lsv2_pt_8cad5_87bd7192b1"
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_PROJECT = "medical-Chatbot"
PINECONE_API_KEY = "pcsLH4u"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
```

### step-8 
Store Embeddings in Pinecone
```bash
python store_index.py
```

### step-9 
```bash
python app.py 
``` 

## How It Works 

This chatbot follows a **Retrieval-Augmented Generation (RAG)** architecture to provide accurate medical answers by combining document retrieval with Large Language Models.

### 1️. Document Processing
Medical PDF documents are loaded from the dataset and split into smaller text chunks to improve retrieval accuracy.

### 2️. Embedding Generation
Each text chunk is converted into **vector embeddings** using an embedding model.  
These embeddings capture the semantic meaning of the text.

### 3️. Vector Storage
The embeddings are stored in the **Pinecone vector database**, enabling fast similarity search.

### 4️. User Query
When a user asks a medical question through the chatbot interface, the query is also converted into an embedding.

### 5️. Context Retrieval
The system searches Pinecone to retrieve the most relevant document chunks related to the query.

### 6️. LLM Response Generation
The retrieved context is passed to a **Large Language Model (LLM)** which generates a final response using the relevant medical information.

### 7️. Response Delivery
The generated answer is displayed to the user through the **Flask-based web chatbot interface**.


##  Architecture

The Medical Chatbot follows a **Retrieval-Augmented Generation (RAG)** architecture that combines document retrieval with a Large Language Model to generate accurate responses.

### System Workflow

1. **Document Loading**
   - Medical PDF documents are loaded from the dataset.

2. **Text Chunking**
   - Documents are split into smaller chunks using a text splitter to improve retrieval efficiency.

3. **Embedding Generation**
   - Each chunk is converted into vector embeddings using an embedding model.

4. **Vector Storage**
   - The embeddings are stored in the **Pinecone vector database** for fast similarity search.

5. **User Query Processing**
   - When a user asks a question, the query is converted into an embedding.

6. **Similarity Search**
   - Pinecone retrieves the most relevant document chunks related to the query.

7. **LLM Response Generation**
   - Retrieved context is sent to the **Large Language Model (LLM)** using **LangChain**.

8. **Monitoring with LangSmith**
   - LangSmith is used for tracing, debugging, and monitoring the LLM workflow.

9. **Response Delivery**
   - The final answer is displayed through the **Flask web interface**.


##  Example Use Cases

The Medical Chatbot can assist users with various healthcare-related queries by retrieving relevant medical knowledge and generating clear explanations.

1️. **Disease Information**
- Example: *“What is abdominal ultrasound and when is it used?”*

2️. **Symptoms Understanding**
- Example: *“What symptoms indicate liver disease?”*

3️. **Diagnostic Test Explanation**
- Example: *“How does an ultrasound scan work in diagnosing abdominal problems?”*

4️. **Medical Procedure Guidance**
- Example: *“What happens during an abdominal ultrasound procedure?”*

5️. **Treatment Information**
- Example: *“What treatments are available for gallstones?”*

6️. **Medical Terminology Explanation**
- Example: *“What does cirrhosis mean in medical terms?”*

7️. **Disease Causes and Risk Factors**
- Example: *“What causes kidney disease?”*

8️. **Prevention and Health Awareness**
- Example: *“How can abdominal diseases be prevented?”*

9️. **Medical Imaging Knowledge**
- Example: *“How does ultrasound differ from CT scans?”*

10. **General Medical Knowledge Assistance**
- Example: *“Explain abdominal aortic aneurysm in simple terms.”*


###  Components Used

- **LangChain** → Orchestrates the LLM workflow  
- **Pinecone** → Vector database for semantic search  
- **Gemini / LLM** → Generates responses  
- **Flask** → Web interface for the chatbot  
- **LangSmith** → Monitoring and debugging LLM pipelines


