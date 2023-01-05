from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.SJQuestion import SJQuestion
from Utilities.Documents.SJ_Docx import SJ_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/SJ/ukcat18sj252.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = SJQuestion(soup, os.path.dirname(file_path))
    doc = SJ_Docx()
    output = doc.generate_template(question)
    output.save(question.get_document_name())