from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.ARType4Question import ARType4Question
from Utilities.Documents.AR_Docx import AR_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/AR/ucat19ar165/ucat19ar165.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = ARType4Question(soup, os.path.dirname(file_path))
    doc = AR_Docx()
    output = doc.generate_type_4_template(question)
    output.save(question.get_document_name())