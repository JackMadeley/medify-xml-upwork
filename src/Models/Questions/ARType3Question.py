from bs4 import BeautifulSoup, Tag

from Models.Questions.Question import Question
from Utilities.XML.General_Question_XML import General_Question_XML
from Utilities.XML.DM_XML import DM_XML


class ARType3Question(Question):

    def __init__(self, soup: BeautifulSoup, directory_path: str):
        super().__init__()
        question: Tag = soup.find_all(name="question")[0]
        self.item_name = General_Question_XML.get_item_name_from_soup(soup)
        self.category = General_Question_XML.get_category_name_from_soup(soup)
        self.question = DM_XML.get_question_from_tag(question, directory_path)
        self.question_stem = General_Question_XML.get_question_stem_from_tag(question, directory_path)
        self.answer_choice_set = General_Question_XML.get_answer_choice_set_from_tag(question, directory_path)
        self.explanation = General_Question_XML.get_explanation_from_tag(question, directory_path)