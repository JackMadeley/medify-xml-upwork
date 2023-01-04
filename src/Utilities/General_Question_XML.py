from typing import List

from bs4 import BeautifulSoup, Tag

from Models.Components.AnswerChoice import AnswerChoice
from Utilities.General_XML import General_XML


class General_Question_XML:

    @staticmethod
    def get_category_name_from_soup(soup: BeautifulSoup) -> str:
        category_name = soup.find_all("catref-ukcat-qtopic")[0]["categoryname"]
        return category_name

    @staticmethod
    def get_category_name_from_tag(tag: Tag) -> str:
        category_refs = list(filter(lambda x: x.name == 'categoryrefs', list(filter(lambda x: isinstance(x, Tag),
                                                                                    tag.contents))))[0].contents
        catref_ukcat_qtopic = list(filter(lambda x: x.name == 'catref-ukcat-qtopic', list(filter(lambda x:
                                                                                                 isinstance(x, Tag),
                                                                                                 category_refs))))[0]
        try:
            return catref_ukcat_qtopic["categoryname"]
        except KeyError:
            raise Exception("Could not find category name attr in tag")

    @staticmethod
    def get_stimulus_from_soup(soup: BeautifulSoup, directory_path: str) -> List[object]:
        stimulus = soup.find_all(name="stimulus")[0].contents
        stimulus_objects = General_XML.parse_component_to_object(stimulus, directory_path)
        return stimulus_objects

    @staticmethod
    def get_question_stem_from_tag(tag: Tag, directory_path: str) -> List[object]:
        question_stem = list(filter(lambda x: x.name == 'question-stem', list(filter(lambda x: isinstance(x, Tag),
                                                                                     tag.contents))))[0].contents
        question_stem_contents = General_XML.parse_component_to_object(question_stem, directory_path)
        return question_stem_contents

    @staticmethod
    def get_answer_choice_set_from_tag(tag: Tag, directory_path: str) -> List[AnswerChoice]:
        answer_choice_set: List[Tag] = list(filter(lambda x: x.name == 'answer-choice-set',
                                                   list(filter(lambda x: isinstance(x, Tag),
                                                               tag.contents))))[0].contents
        answer_choices: List[Tag] = list(filter(lambda x: x.name == 'answer-choice', answer_choice_set))
        output: List[AnswerChoice] = []
        for choice in answer_choices:
            output.append(AnswerChoice(choice, directory_path))
        return output

    @staticmethod
    def get_explanation_from_tag(tag: Tag, directory_path: str) -> List[object]:
        explanation: List[Tag] = list(filter(lambda x: x.name == 'explanation',
                                             list(filter(lambda x: isinstance(x, Tag), tag.contents))))[0].contents
        explanation_contents = General_XML.parse_component_to_object(explanation, directory_path)
        return explanation_contents

    @staticmethod
    def get_item_name_from_soup(soup: BeautifulSoup) -> str:
        question_set = soup.find_all(name="question")[0]
        return question_set["contentitemname"]

