# PDF_loader
<h1>PDF Document Loader with LangChain</h1>

<p>
This project demonstrates how to load and extract text from a PDF using
<strong>LangChain's PyPDFLoader</strong>.
</p>

<h2>What I Learned</h2>

<ul>
  <li>How a PDF is loaded using <code>PyPDFLoader</code>.</li>
  <li>How <code>loader.load()</code> converts the PDF into a list of LangChain <code>Document</code> objects.</li>
  <li>Each <code>Document</code> contains <code>page_content</code> and <code>metadata</code>.</li>
  <li><code>page_content</code> contains the extracted text from the PDF.</li>
  <li><code>metadata</code> contains information such as the source file, page number, author, and total pages.</li>
</ul>

<h2>Basic Flow</h2>

<pre>
PDF File
   ↓
PyPDFLoader
   ↓
loader.load()
   ↓
Document Objects
   ├── page_content
   └── metadata
</pre>

<h2>Example</h2>

<pre><code>from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("check.pdf")

documents = loader.load()

print(documents[0].page_content)
print(documents[0].metadata)</code></pre>

<h2>Key Concept</h2>

<p>
A <strong>Document Loader</strong> is used to load data from a source and
convert it into LangChain <code>Document</code> objects. These documents can
then be passed to a text splitter, embedding model, vector database, and
retriever as part of a RAG pipeline.
</p>

<h2>RAG Connection</h2>

<pre>
PDF
 ↓
Document Loader
 ↓
Documents
 ↓
Text Splitter
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
LLM
</pre>

<p>
<strong>Learning Level:</strong> MUST KNOW for a GenAI/RAG Developer.
</p>
