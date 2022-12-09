from bs4 import BeautifulSoup
from Utilities.XML import XML


class SingleAnswerQuestion(object):

    def __init__(self, soup: BeautifulSoup, directory: str):
        self.category_name = XML.get_category_name(soup)
        self.question = XML.get_question_contents(soup, directory)
        self.question_stem = XML.get_question_stem_contents(soup, directory)
        self.answers = XML.get_answer_set_contents(soup, directory)
        self.explanation = XML.get_explanation_contents(soup, directory)


