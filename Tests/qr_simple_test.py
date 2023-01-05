from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.QRSimpleQuestion import QRSimpleQuestion
from Utilities.Documents.QR_Docx import QR_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/QR/ukcatmstryqr1808.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = QRSimpleQuestion(soup, os.path.dirname(file_path))
    doc = QR_Docx()
    output = doc.generate_simple_template(question)
    output.save(question.get_document_name())