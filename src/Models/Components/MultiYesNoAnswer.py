from bs4 import Tag
from typing import List


class MultiYesNoAnswer(object):

    def __init__(self, tag: Tag, contents: List[object]):
        self.answer = MultiYesNoAnswer.get_answer_bool(tag=tag)
        self.contents = contents

    @staticmethod
    def get_answer_bool(tag: Tag) -> bool:
        try:
            correct_str: str = tag["answer"]
            if correct_str.lower().strip() == "yes":
                return True
            else:
                return False
        except KeyError:
            raise Exception("Could not find the answer for the ")