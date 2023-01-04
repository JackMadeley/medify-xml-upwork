from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.SJQuestion import SJQuestion

file_path = "/home/jm/Downloads/Kaplan XML Extraction/SJ/ukcat18sj252.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = SJQuestion(soup, os.path.dirname(file_path))
    print(question)
