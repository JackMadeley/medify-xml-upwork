import unicodedata
from typing import List

from Models.Components.AnswerChoice import AnswerChoice
from Models.Components.Emphasis import Emphasis
from Models.Components.Graphic import Graphic
from bs4 import BeautifulSoup, Tag, NavigableString

from Models.Components.MultiYesNoAnswer import MultiYesNoAnswer


class XML:

    @staticmethod
    def get_character_dict() -> dict:
        return {
            "divide": unicodedata.lookup("Division Sign"),
            "rsquo": unicodedata.lookup("Right Single Quotation Mark"),
            "lsquo": unicodedata.lookup("Left Single Quotation Mark"),
            "ndash": unicodedata.lookup("En Dash"),
            "pound": unicodedata.lookup("Pound Sign")
        }

    @staticmethod
    def get_item_name(soup: BeautifulSoup) -> str:
        return soup.find_all("question")[0]['contentitemname']

    @staticmethod
    def get_category_name(soup: BeautifulSoup):
        category_name = soup.find_all("catref-ukcat-qtopic")[0]["categoryname"]
        return category_name

    @staticmethod
    def parse_contents_to_object(contents: List[object], directory: str) -> List[object]:
        output = []
        for tag in contents:
            if isinstance(tag, NavigableString):
                if tag.text == "\n":
                    pass
                else:
                    output.append(tag.text.replace("\n", " ").strip().replace("?", "? ").replace(".", ". ")
                                  .replace("!", "! "))
            elif isinstance(tag, Tag):
                if tag.name == 'categoryrefs':
                    pass
                elif tag.name == 'question-stem':
                    pass
                elif tag.name == 'multi-yesno-questions':
                    pass
                elif tag.name == 'explanation':
                    pass
                elif tag.name == 'answer-choice-set':
                    pass
                elif tag.name == "para":
                    output.extend(XML.parse_contents_to_object(tag.contents, directory))
                elif tag.name == "figure":
                    output.extend(XML.parse_contents_to_object(tag.contents, directory))
                elif tag.name == "br":
                    pass
                elif tag.name == "graphic":
                    output.append(Graphic(tag, directory))
                elif tag.name == "yesno-question":
                    output.extend(XML.parse_contents_to_object(tag.contents, directory))
                elif tag.name == "entity":
                    character_dict = XML.get_character_dict()
                    try:
                        character = character_dict[tag.text]
                        output.append(character)
                    except KeyError:
                        Exception(f"Could not find character {tag.text} in the character dictionary")
                elif tag.name == "emphasis":
                    output.append(Emphasis(tag))
                elif tag.name == "list":
                    output.extend(XML.parse_contents_to_object(tag.contents, directory))
                elif tag.name == "listitem":
                    output.extend(XML.parse_contents_to_object(tag.contents, directory))
                else:
                    raise Exception(f"Unexpected for tag {tag.name}")
            else:
                raise Exception("Unhandled type")
        return output

    @staticmethod
    def get_question_contents(soup: BeautifulSoup, directory: str) -> List[object]:
        question = soup.find_all(name="question")[0].contents
        output = XML.parse_contents_to_object(question, directory)
        return output

    @staticmethod
    def get_question_stem_contents(soup: BeautifulSoup, directory: str) -> List[object]:
        stem = soup.find_all(name="question-stem")[0].contents
        output = XML.parse_contents_to_object(stem, directory)
        return output

    @staticmethod
    def get_answer_set_contents(soup: BeautifulSoup, directory: str) -> List[AnswerChoice]:
        choices = soup.find_all(name="answer-choice-set")[0].contents
        filtered_choices = list(filter(lambda x: isinstance(x, Tag), choices))
        output = []
        for tag in filtered_choices:
            if tag.name == "answer-choice":
                answer_contents = XML.parse_contents_to_object(tag.contents, directory)
                output.append(AnswerChoice(tag, answer_contents))
            else:
                raise Exception(f"Unexpected tag found {tag.name}")
        return output

    @staticmethod
    def get_explanation_contents(soup: BeautifulSoup, directory: str) -> List[object]:
        explanation = soup.find_all(name="explanation")[0].contents
        output = XML.parse_contents_to_object(explanation, directory)
        return output

    @staticmethod
    def get_multi_answer_choice_contents(soup: BeautifulSoup, directory: str) -> List[MultiYesNoAnswer]:
        contents = soup.find_all(name="multi-yesno-questions")[0].contents
        output = []
        filtered_contents = list(filter(lambda x: isinstance(x, Tag), contents))
        for tag in filtered_contents:
            answer_contents = XML.parse_contents_to_object(tag.contents, directory)
            output.append(MultiYesNoAnswer(tag, answer_contents))
        return output
