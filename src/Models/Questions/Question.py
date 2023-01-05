class Question(object):

    def __init__(self):
        self.item_name = None
        self.category = None

    def get_document_name(self):
        return f"{self.item_name} ({self.category}).docx"