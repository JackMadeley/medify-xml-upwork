from bs4 import Tag
from Utilities.XML.General_XML import General_XML


class AnswerChoice(object):

    def __init__(self, tag: Tag, directory_path: str):
        self.correct: bool = AnswerChoice.get_correct_bool(tag)
        self.contents = General_XML.parse_component_to_object(tag.contents, directory_path)

    @staticmethod
    def get_correct_bool(tag: Tag) -> bool:
        try:
            correct_str: str = tag["correct"]
            if correct_str.lower().strip() == "yes":
                return True
            else:
                return False
        except KeyError:
            return False
