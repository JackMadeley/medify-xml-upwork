from typing import List

from bs4 import Tag


class XMLList(object):

    def __init__(self, tag: Tag, contents: List[object]):
        self.prefix = tag['prefix']
        self.list_items = contents
