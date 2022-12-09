import os.path

from bs4 import BeautifulSoup, Tag

from Models.Input.Components.AnswerChoice import AnswerChoice
from Models.Input.Questions.SingleAnswerQuestion import SingleAnswerQuestion
from Utilities.XML import XML


def testing(file_path: str):
    with open(file_path) as file:
        file_data = file.read()
        directory = os.path.dirname(file_path)
        soup = BeautifulSoup(file_data, "lxml")
        obj = SingleAnswerQuestion(soup, directory)
        print("Hello World!")





file_path = r"/home/jm/Documents/DM XML Extraction/ukcat18dm007/ukcat18dm007.xml"

testing(file_path)
