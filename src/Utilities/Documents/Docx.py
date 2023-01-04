import os
from typing import List

from docx.shared import Inches
from docx.table import Table

from Models.Components.Emphasis import Emphasis
from Models.Components.Graphic import Graphic
from Models.Components.Para import Para
from Models.Components.YesNoAnswerChoice import YesNoAnswerChoice


class Docx(object):

    def __init__(self):
        self.template_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Templates")
        self.paragraph_number = 0
