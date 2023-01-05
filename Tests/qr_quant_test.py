from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.QRQuantQuestion import QRQuantQuestion
from Utilities.Documents.QR_Docx import QR_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/QR/ukcat18qr001.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = QRQuantQuestion(soup, os.path.dirname(file_path))
    doc = QR_Docx()
    output = doc.generate_quant_template(question)
    output.save(question.get_document_name())