from typing import List

from bs4 import BeautifulSoup

from Models.Components.QuestionSetMember import QuestionSetMember


class VR_XML:

    @staticmethod
    def get_item_name(soup: BeautifulSoup) -> str:
        question_set = soup.find_all(name="question-set")[0]
        return question_set["contentitemname"]

    @staticmethod
    def get_question_set_members(soup: BeautifulSoup, directory_path: str) -> List[QuestionSetMember]:
        question_set_members = soup.find_all(name="question-set-member")
        output: List[QuestionSetMember] = []
        for question_set_member in question_set_members:
            output.append(QuestionSetMember(question_set_member, directory_path))
        return output


