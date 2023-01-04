from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.DMFiveAnswerQuestion import DMFiveAnswerQuestion

file_path = "/home/jm/Downloads/Kaplan XML Extraction/DM/ukcat18dm074/ukcat18dm074.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = DMFiveAnswerQuestion(soup, os.path.dirname(file_path))
    print(question)
