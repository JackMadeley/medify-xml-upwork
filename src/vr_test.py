from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.VRQuestion import VRQuestion

file_path = "/home/jm/Downloads/Kaplan XML Extraction/VR/ukcat18vr001.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = VRQuestion(soup, os.path.dirname(file_path))
    print(question)
