from sources.common import logger, logProc, processControl, log_
import os
import re
from PyPDF2 import PdfReader
from transformers import pipeline


def summarize_text(text, max_length=50):
    """
    Summarizes the accumulated text using a pre-trained summarizer.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=20, do_sample=False)
    return summary[0]["summary_text"]

def processSummarize(text):
    if text.strip():
        log_("info", logger, "Summarizing accumulated text...")
        summary = summarize_text(text)
        print("\nSummary:\n", summary)
    else:
        print("No valid 'Introduction' sections found to summarize.")
    return summary

