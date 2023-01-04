from bs4 import BeautifulSoup, Tag

from Utilities.DM_XML import DM_XML
from Utilities.General_Question_XML import General_Question_XML


class QRSimpleQuestion(object):

    def __init__(self, soup: BeautifulSoup, directory_path: str):
        question: Tag = soup.find_all(name="question")[0]
        self.item_name = General_Question_XML.get_item_name_from_soup(soup)
        self.category = General_Question_XML.get_category_name_from_soup(soup)
        self.stimulus = General_Question_XML.get_stimulus_from_soup(soup, directory_path)
        self.question_stem = General_Question_XML.get_question_stem_from_tag(question, directory_path)
        self.answer_choice_set = General_Question_XML.get_answer_choice_set_from_tag(question, directory_path)
        self.explanation = General_Question_XML.get_explanation_from_tag(question, directory_path)
