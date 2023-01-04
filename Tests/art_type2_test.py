from bs4 import BeautifulSoup, Tag
import lxml
import os

from Models.Questions.ARType2Question import ARType2Question

file_path = "/home/jm/Downloads/Kaplan XML Extraction/AR/ucat19ar169/ucat19ar169.xml"

with open(file_path) as file:
    file_data = file.read()
    soup = BeautifulSoup(file_data, "lxml")
    question = ARType2Question(soup, os.path.dirname(file_path))
    print(question)
