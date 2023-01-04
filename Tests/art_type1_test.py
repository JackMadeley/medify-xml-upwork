from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.ARType1Question import ARType1Question

file_path = "/home/jm/Downloads/Kaplan XML Extraction/AR/ucat19ar159/ucat19ar159.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = ARType1Question(soup, os.path.dirname(file_path))
    print(question)
