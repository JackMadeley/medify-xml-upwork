from bs4 import Tag
from typing import List

from Models.Components.YesNoAnswerChoice import YesNoAnswerChoice
from Utilities.XML.General_XML import General_XML


class DM_XML:

    @staticmethod
    def get_question_from_tag(tag: Tag, directory_path: str ):
        start_tag_name = "categoryrefs"
        end_tag_name = "question-stem"
        selected: List[Tag] = []
        capture = False
        for tag in tag.contents:
            if isinstance(tag, Tag):
                if tag.name == end_tag_name:
                    capture = False
                if capture:
                    selected.append(tag)
                if tag.name == start_tag_name:
                    capture = True
        output = General_XML.parse_component_to_object(selected, directory_path)
        return output

    @staticmethod
    def get_multi_answer_from_tag(tag: Tag, directory_path: str):
        answer_choice_set: List[Tag] = list(filter(lambda x: x.name == 'multi-yesno-questions',
                                                   list(filter(lambda x: isinstance(x, Tag),
                                                               tag.contents))))[0].contents
        answer_choices: List[Tag] = list(filter(lambda x: x.name == 'yesno-question', answer_choice_set))
        output: List[YesNoAnswerChoice] = []
        for choice in answer_choices:
            output.append(YesNoAnswerChoice(choice, directory_path))
        return output
