from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.DMFiveAnswerQuestion import DMFiveAnswerQuestion
from Utilities.Documents.DM_Docx import DM_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/DM/ukcat18dm074/ukcat18dm074.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = DMFiveAnswerQuestion(soup, os.path.dirname(file_path))
    doc = DM_Docx()
    output = doc.generate_five_part_question(question)
    output.save("test.docx")
    print(question)
