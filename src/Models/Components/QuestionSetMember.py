from bs4 import Tag
from Utilities.XML.General_Question_XML import General_Question_XML


class QuestionSetMember(object):

    def __init__(self, tag: Tag, directory_path: str):
        self.item_name = tag["contentitemname"]
        self.category = General_Question_XML.get_category_name_from_tag(tag)
        self.question_stem = General_Question_XML.get_question_stem_from_tag(tag, directory_path)
        self.answer_choice_set = General_Question_XML.get_answer_choice_set_from_tag(tag, directory_path)
        self.explanation = General_Question_XML.get_explanation_from_tag(tag, directory_path)
