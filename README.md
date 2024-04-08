PDF Document Analysis and Question Generation
Overview
This project aims to develop a Python script that analyzes PDF documents and generates questions based on their content using Natural Language Processing (NLP) techniques. The script extracts text from uploaded PDF files, processes the text data using spaCy library for NLP tasks, and generates questions to assess the content comprehension.

Features
PDF Text Extraction: Extracts text content from PDF documents using PyPDF2 library.
NLP Processing: Utilizes spaCy library for tokenization, part-of-speech tagging, and sentence boundary detection.
Question Generation: Generates questions based on extracted text by identifying nouns and verbs in sentences.
Multi-language Support: Supports PDF documents in multiple languages for analysis and question generation.
Requirements
Python 3.x
PyPDF2 library
spaCy library with English language model (en_core_web_sm)
Installation
Install Python 3.x from python.org.
Install required libraries:
Copy code
pip install PyPDF2 spacy
python -m spacy download en_core_web_sm
Usage
Clone or download the project repository.
Place your PDF documents in the project folder.
Run the script using Python:
Copy code
python pdf_analysis.py
The script will analyze the PDF documents and generate questions based on their content.
View the generated questions in the console output or in the output file.
Contributors
Your Name
License
This project is licensed under the MIT License.
