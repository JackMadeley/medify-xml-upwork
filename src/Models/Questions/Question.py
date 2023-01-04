from bs4 import BeautifulSoup

from Utilities.General_Question_XML import General_Question_XML
from Utilities.VR_XML import VR_XML


class Question(object):

    def __init__(self):
        self.item_name = None
        self.category = None

    def get_document_name(self):
        return f"{self.item_name} ({self.category})"