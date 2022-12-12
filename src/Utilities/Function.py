from bs4 import BeautifulSoup
import os
from Models.Questions.SingleAnswerQuestion import SingleAnswerQuestion
from Models.Questions.FiveAnswerQuestion import FiveAnswerQuestion
from Utilities.WordDocument import WordDocument
import re


class Function:

    @staticmethod
    def determine_five_part_question(soup: BeautifulSoup) -> bool:
        try:
            results = soup.find_all("multi-yesno-questions")
            if len(results) > 0:
                return True
            else:
                return False
        except KeyError:
            return False

    @staticmethod
    def generate_docx(file_path: str):
        with open(file_path) as file:
            file_data = file.read()
            directory = os.path.dirname(file_path)
            soup = BeautifulSoup(file_data, "lxml")
            five_part_question = Function.determine_five_part_question(soup)
            if five_part_question:
                obj = FiveAnswerQuestion(soup, directory)
                file_name = WordDocument.get_document_name(obj)
                output_path = os.path.join(directory, file_name)
                WordDocument.generate_five_answer_question_document(obj, output_path)
            else:
                obj = SingleAnswerQuestion(soup, directory)
                file_name = WordDocument.get_document_name(obj)
                output_path = os.path.join(directory, file_name)
                WordDocument.generate_single_answer_question_document(obj, output_path)

    @staticmethod
    def run(folder: str):
        if os.path.exists(folder):
            result = []
            reg_compile = re.compile(".*.xml")
            for file in os.listdir(folder):
                if reg_compile.match(file):
                    result.append(os.path.join(folder, file))
            if len(result) == 0:
                print("Could not find any XML files in the directory provided, please try again")
            else:
                for file in result:
                    Function.generate_docx(file)
        else:
            print("Could not find the directory entered, please try again")