from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.ARType4Question import ARType4Question

file_path = "/home/jm/Downloads/Kaplan XML Extraction/AR/ucat19ar165/ucat19ar165.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = ARType4Question(soup, os.path.dirname(file_path))
    print(question)
