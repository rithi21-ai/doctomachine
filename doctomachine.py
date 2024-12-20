import os
import PyPDF2
from docx import Document

def read_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {e}")
    return text

def read_docx(file_path):
    """Extract text from a DOCX file."""
    text = ""
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX file {file_path}: {e}")
    return text

def read_txt(file_path):
    """Extract text from a TXT file."""
    text = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading TXT file {file_path}: {e}")
    return text

def save_to_file(output_path, content):
    """Save extracted content to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content saved to {output_path}")
    except Exception as e:
        print(f"Error saving content to file {output_path}: {e}")

def process_file(file_path, output_dir):
    """Process a single file and extract text."""
    extension = os.path.splitext(file_path)[-1].lower()
    content = ""

    if extension == '.pdf':
        content = read_pdf(file_path)
    elif extension == '.docx':
        content = read_docx(file_path)
    elif extension == '.txt':
        content = read_txt(file_path)
    else:
        print(f"Unsupported file type: {file_path}")
        return

    # Save extracted text to output file
    if content:
        base_name = os.path.basename(file_path)
        output_path = os.path.join(output_dir, f"{os.path.splitext(base_name)[0]}_output.txt")
        save_to_file(output_path, content)

def main(input_dir, output_dir):
    """Process all files in the input directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if os.path.isfile(file_path):
            process_file(file_path, output_dir)

if __name__ == "__main__":
    input_directory = input("Enter the path to the input directory: ").strip()
    output_directory = input("Enter the path to the output directory: ").strip()
    main(input_directory, output_directory)
