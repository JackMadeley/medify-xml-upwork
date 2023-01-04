from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.DMSingleAnswerQuestion import DMSingleAnswerQuestion

file_path = "/home/jm/Downloads/Kaplan XML Extraction/DM/ukcat18dm020/ukcat18dm020.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = DMSingleAnswerQuestion(soup, os.path.dirname(file_path))
    print(question)
