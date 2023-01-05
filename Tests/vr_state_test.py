from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.VRQuestion import VRQuestion
from Utilities.Documents.VR_Docx import VR_Docx

file_path = "/home/jm/Downloads/Kaplan XML Extraction/VR/ukcat18vr013.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = VRQuestion(soup, os.path.dirname(file_path))
    doc = VR_Docx()
    output = doc.generate_state_template(question)
    output.save(question.get_document_name())