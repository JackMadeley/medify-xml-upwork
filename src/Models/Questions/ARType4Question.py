from bs4 import BeautifulSoup

from Models.Questions.Question import Question
from Utilities.General_Question_XML import General_Question_XML
from Utilities.VR_XML import VR_XML


class ARType4Question(Question):

    def __init__(self, soup: BeautifulSoup, directory_path: str):
        super().__init__()
        self.item_name = VR_XML.get_item_name(soup)
        self.category = General_Question_XML.get_category_name_from_soup(soup)
        self.stimulus = General_Question_XML.get_stimulus_from_soup(soup, directory_path)
        self.question_set_members = VR_XML.get_question_set_members(soup, directory_path)