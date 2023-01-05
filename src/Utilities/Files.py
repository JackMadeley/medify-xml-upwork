import re
import os
from pathlib import Path

from bs4 import BeautifulSoup

from Models.Questions.ARType1Question import ARType1Question
from Models.Questions.ARType2Question import ARType2Question
from Models.Questions.ARType3Question import ARType3Question
from Models.Questions.ARType4Question import ARType4Question
from Models.Questions.DMFiveAnswerQuestion import DMFiveAnswerQuestion
from Models.Questions.DMSingleAnswerQuestion import DMSingleAnswerQuestion
from Models.Questions.QRSimpleQuestion import QRSimpleQuestion
from Models.Questions.QRQuantQuestion import QRQuantQuestion
from Models.Questions.VRQuestion import VRQuestion
from Models.Questions.SJQuestion import SJQuestion
from Utilities.Documents.AR_Docx import AR_Docx
from Utilities.Documents.DM_Docx import DM_Docx
from Utilities.Documents.QR_Docx import QR_Docx
from Utilities.Documents.SJ_Docx import SJ_Docx
from Utilities.Documents.VR_Docx import VR_Docx
from Utilities.XML.General_Question_XML import General_Question_XML


class Function:

    @staticmethod
    def loop_through_directory_recursive(directory: str):
        for file in Path(directory).glob('**/*.xml'):
            try:
                Function.generate_question(file)
                print(f"Success: {file}")
            except Exception as ex:
                print(f"Fail: {file}")
                print(ex)

    @staticmethod
    def generate_question(file_path: str):
        file_name = os.path.basename(file_path).split(os.sep)[-1]
        directory_path = os.path.dirname(file_path)
        match = re.match("ukcat[0-9]+([a-z][a-z])[0-9]+.xml", file_name)
        if match is None:
            match = re.match("ucat[0-9]+([a-z][a-z])[0-9]+.xml", file_name)
        if match is None:
            match = re.match("ukcatmstry([a-z][a-z])[0-9]+.xml", file_name)
        if match is None:
            raise Exception("Could not find matching regex pattern in file name")
        group = match.groups()[0]
        soup: BeautifulSoup
        with open(file_path) as file:
            file_data = file.read()
            soup = BeautifulSoup(file_data, "lxml")
        category_ref = General_Question_XML.get_category_name_from_soup(soup)
        if group == "dm":
            doc = DM_Docx()
            if category_ref == "decis.vendiaq" or category_ref == "decis.logpuz" or category_ref == "decis.strgargq"\
                    or category_ref == "decis.mathq":
                question = DMSingleAnswerQuestion(soup, directory_path)
                output = doc.generate_single_part_question(question)
            elif category_ref == "decis.syllogism" or category_ref == "decis.infer":
                question = DMFiveAnswerQuestion(soup, directory_path)
                output = doc.generate_five_part_question(question)
            else:
                raise Exception(f"An unexpected DM type {category_ref} was discovered")
        elif group == "ar":
            doc = AR_Docx()
            if category_ref == "abstr.type1":
                question = ARType1Question(soup, directory_path)
                output = doc.generate_type_1_template(question)
            elif category_ref == "abstr.type2":
                question = ARType2Question(soup, directory_path)
                output = doc.generate_type_2_template(question)
            elif category_ref == "abstr.type3":
                question = ARType3Question(soup, directory_path)
                output = doc.generate_type_3_template(question)
            elif category_ref == "abstr.type4":
                question = ARType4Question(soup, directory_path)
                output = doc.generate_type_4_template(question)
            else:
                raise Exception(f"An unexpected AR type {category_ref} was discovered")
        elif group == "qr":
            doc = QR_Docx()
            if category_ref == "quant.quant":
                question = QRQuantQuestion(soup, directory_path)
                output = doc.generate_quant_template(question)
            elif category_ref == "quant.simple":
                question = QRSimpleQuestion(soup, directory_path)
                output = doc.generate_simple_template(question)
            else:
                raise Exception(f"An unexpected QR type {category_ref} was discovered")
        elif group == "sj":
            doc = SJ_Docx()
            question = SJQuestion(soup, directory_path)
            output = doc.generate_template(question)
        elif group == "vr":
            doc = VR_Docx()
            question = VRQuestion(soup, directory_path)
            if category_ref == "verb.ques":
                output = doc.generate_question_template(question)
            elif category_ref == "verb.state":
                output = doc.generate_state_template(question)
            else:
                raise Exception(f"An unexpected VR type {category_ref} was discovered")
        output.save(os.path.join(directory_path, question.get_document_name()))
