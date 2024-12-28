from sources.common import logger, logProc, processControl, log_
import os
import re
from PyPDF2 import PdfReader
from transformers import pipeline

def extract_introduction_text(pdf_path):
    """
    Extracts text from the 'Introduction' chapter of a PDF.
    Assumes 'Introduction' is the chapter header followed by text
    until the next chapter or the end of the document.
    """
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text()

        # Regular expression to capture the "Introduction" section
        intro_pattern = r"(?:\bIntroduction\b.*?)(.*?)(?:\n\b[A-Z][a-zA-Z]+\b|\Z)"
        match = re.search(intro_pattern, full_text, re.DOTALL)

        if match:
            return match.group(1).strip()
        else:
            print(f"No 'Introduction' found in: {pdf_path}")
            return ""
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return ""


def processExtract():
    """
    Main function to extract text from the 'Introduction' chapters of
    PDFs in the directory, accumulate the text, and generate a summary.
    """

    accumulated_text = ""
    directoryPath = processControl.env['inputPath']

    for filename in os.listdir(directoryPath):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directoryPath, filename)
            log_("info", logger, f"Processing {file_path}...")
            intro_text = extract_introduction_text(file_path)
            if intro_text:
                accumulated_text += intro_text + "\n"

    return accumulated_text
