from bs4 import Tag


class Emphasis:

    def __init__(self, tag: Tag):
        self.bold = False
        self.italic = False
        self.underline = False
        self.set_attrs(tag)
        self.text = tag.text

    def set_attrs(self, tag: Tag):
        try:
            emphasis_type = tag["emphasis-type"]
            if emphasis_type == "bold":
                self.bold = True
            elif emphasis_type == "italic":
                self.italic = True
            elif emphasis_type == "underline":
                self.underline = True
            else:
                raise Exception(f"Unknown emphasis type {emphasis_type}")
        except KeyError:
            raise Exception("Could not find emphasis type attribute")

