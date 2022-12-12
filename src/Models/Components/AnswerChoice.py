from typing import List

from bs4 import Tag


class AnswerChoice(object):

    def __init__(self, tag: Tag, contents: List[object]):
        self.correct: bool = AnswerChoice.get_correct_bool(tag)
        self.contents = contents

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
