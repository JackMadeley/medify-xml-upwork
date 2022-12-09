from bs4 import Tag


class MultiYesNoAnswer(object):

    def __init__(self, tag: Tag, directory: str):
        self.answer = MultiYesNoAnswer.get_answer_bool(tag=tag)


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