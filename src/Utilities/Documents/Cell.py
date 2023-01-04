from typing import List

from docx.shared import Inches
from docx.table import Table

from Models.Components.Emphasis import Emphasis
from Models.Components.Graphic import Graphic
from Models.Components.Para import Para
from Models.Components.YesNoAnswerChoice import YesNoAnswerChoice


class Cell(object):

    def __init__(self, table: Table):
        self.table = table
        self.paragraph_number = 0

    def add_contents_to_cells(self, contents: List[object]):
        for item in contents:
            current_type = type(item)
            if current_type is str:
                self.table.paragraphs[self.paragraph_number].add_run(text=item)
            elif current_type is Para:
                self.add_contents_to_cells(item.contents)
                self.table.add_paragraph()
                self.paragraph_number += 1
            elif current_type is Graphic:
                self.table.paragraphs[self.paragraph_number].add_run().add_picture(image_path_or_stream=item.path,
                                                                                  width=Inches(5))
                self.table.add_paragraph()
                self.paragraph_number += 1
            elif current_type is Emphasis:
                if item.bold == True:
                    self.table.paragraphs[0].add_run(f" {item.text} ").bold = True
                elif item.italic == True:
                    self.table.paragraphs[0].add_run(f" {item.text} ").italic = True
                elif item.underline == True:
                    self.table.paragraphs[0].add_run(f" {item.text} ").underline = True
            else:
                raise Exception(f"Unable to determine how to process type {current_type}")

    def set_multi_answer(self, row: int, answer: YesNoAnswerChoice):
        answer_box = Cell(self.table.cell(row, 2))
        yes_no_box = Cell(self.table.cell(row, 5))
        answer_box.add_contents_to_cells(answer.contents)
        if answer.correct:
            yes_no_box.add_contents_to_cells(["Yes"])
        else:
            yes_no_box.add_contents_to_cells(["No"])