from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.DMSingleAnswerQuestion import DMSingleAnswerQuestion
from Utilities.Documents.DM_Docx import DM_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/DM/ukcat18dm020/ukcat18dm020.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = DMSingleAnswerQuestion(soup, os.path.dirname(file_path))
    doc = DM_Docx()
    output = doc.generate_single_part_question(question)
    output.save("test1.docx")
