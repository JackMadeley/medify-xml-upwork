from typing import List

from Models.Input.Components.AnswerChoice import AnswerChoice
from Models.Input.Components.Graphic import Graphic
from bs4 import BeautifulSoup, Tag


class XML:

    @staticmethod
    def get_category_name(soup: BeautifulSoup):
        category_name = soup.find_all("catref-ukcat-qtopic")[0]["categoryname"]
        return category_name

    @staticmethod
    def get_question_content_tags(soup: BeautifulSoup) -> List[Tag]:
        question = soup.find_all(name="question")[0].contents
        valid_tags = list(filter(lambda x: x.name == "para" or x.name == "figure",
                                 list(filter(lambda x: isinstance(x, Tag), question))))
        return valid_tags

    @staticmethod
    def get_explanation_tags(soup: BeautifulSoup) -> List[Tag]:
        explanation = soup.find_all(name="explanation")[0].contents
        tags = list(filter(lambda x: isinstance(x, Tag), explanation))
        return tags

    @staticmethod
    def get_question_stem_tags(soup: BeautifulSoup) -> List[Tag]:
        stem = soup.find_all(name="question-stem")[0].contents
        tags = list(filter(lambda x: isinstance(x, Tag), stem))
        return tags

    @staticmethod
    def get_answer_choice_tags(soup: BeautifulSoup) -> List[Tag]:
        choices = soup.find_all(name="answer-choice-set")[0].contents
        tags = list(filter(lambda x: isinstance(x, Tag), choices))
        return tags

    @staticmethod
    def parse_tags_to_objects(tags: List[Tag], directory: str) -> List[object]:
        output = []
        for tag in tags:
            if tag.name == "para":
                output.append(tag.text)
            elif tag.name == "figure":
                graphic_tags = list(filter(lambda x: x.name == "graphic", tag.contents))
                for graphic_tag in graphic_tags:
                    output.append(Graphic(graphic_tag, directory))
            elif tag.name == "br":
                pass
            elif tag.name == "graphic":
                output.append(Graphic(tag, directory))
            else:
                raise Exception(f"Unexpected for tag {tag.name}")
        return output

    @staticmethod
    def get_question_contents(soup: BeautifulSoup, directory: str) -> List[object]:
        contents = XML.get_question_content_tags(soup)
        output = XML.parse_tags_to_objects(contents, directory)
        return output

    @staticmethod
    def get_question_stem_contents(soup: BeautifulSoup, directory: str) -> List[object]:
        contents = XML.get_question_stem_tags(soup)
        output = XML.parse_tags_to_objects(contents, directory)
        return output

    @staticmethod
    def get_answer_set_contents(soup: BeautifulSoup, directory: str) -> List[AnswerChoice]:
        contents = XML.get_answer_choice_tags(soup)
        output = []
        for tag in contents:
            if tag.name == "answer-choice":
                filtered_contents = list(filter(lambda x: isinstance(x, Tag), tag.contents))
                answer_contents = XML.parse_tags_to_objects(filtered_contents, directory)
                output.append(AnswerChoice(tag, answer_contents))
            else:
                raise Exception(f"Unexpected tag found {tag.name}")
        return output

    @staticmethod
    def get_explanation_contents(soup: BeautifulSoup, directory: str) -> List[object]:
        contents = XML.get_explanation_tags(soup)
        output = XML.parse_tags_to_objects(contents, directory)
        return output
