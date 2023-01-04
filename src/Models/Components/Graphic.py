
from bs4 import Tag
import os


class Graphic(object):

    def __init__(self, tag: Tag, directory: str):
        self.path = Graphic.get_path(tag, directory)

    @staticmethod
    def get_path(tag: Tag, directory: str):
        try:
            graphic_ref_str: str = tag["graphic-ref"]
            path = os.path.join(directory, graphic_ref_str)
            if os.path.exists(path):
                return path
            else:
                raise FileNotFoundError(f"Could not find file at {path}")
        except KeyError:
            raise Exception("Could not find graphic reference link in tag")

    def generate_image(self):
        pass
