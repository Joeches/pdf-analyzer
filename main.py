import PyPDF2
import spacy

# Load the installed spaCy model
nlp = spacy.load("en_core_web_sm")

# Load English language model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF document.

    Parameters:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text


def generate_questions(text):
    """
    Generate questions based on the content of the text.

    Parameters:
        text (str): The text content extracted from the PDF.

    Returns:
        list: A list of generated questions.
    """
    questions = []
    doc = nlp(text)

    # Extract sentences from the text
    sentences = [sent.text.strip() for sent in doc.sents]

    for sentence in sentences:
        # Skip short sentences
        if len(sentence.split()) < 6:
            continue

        # Tokenize the sentence
        tokens = nlp(sentence)

        # Extract nouns and verbs
        nouns = [token.text for token in tokens if token.pos_ == "NOUN"]
        verbs = [token.text for token in tokens if token.pos_ == "VERB"]

        # Generate questions based on nouns and verbs
        if nouns and verbs:
            question = f"What does {' '.join(nouns)} {verbs[0]}?"
            questions.append(question)

    return questions


def main(pdf_file):
    # Extract text from the PDF document
    text = extract_text_from_pdf(pdf_file)

    # Generate questions based on the extracted text
    questions = generate_questions(text)

    # Print the generated questions
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question}")


if __name__ == "__main__":
    # Specify the path to the PDF document
    pdf_file = "example.pdf"

    # Call the main function
    main(pdf_file)
