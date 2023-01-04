import unicodedata
import re
from typing import List

from bs4 import BeautifulSoup, NavigableString, Tag

from Models.Components.Emphasis import Emphasis
from Models.Components.Graphic import Graphic
from Models.Components.XMLList import XMLList



class General_XML:

    @staticmethod
    def get_character_dict() -> dict:
        return {
            "divide": unicodedata.lookup("Division Sign"),
            "rsquo": unicodedata.lookup("Right Single Quotation Mark"),
            "lsquo": unicodedata.lookup("Left Single Quotation Mark"),
            "ndash": unicodedata.lookup("En Dash"),
            "pound": unicodedata.lookup("Pound Sign")
        }

    @staticmethod
    def parse_component_to_object(components: List[object], directory_path: str) -> List[object]:
        output = []
        for tag in components:
            if isinstance(tag, NavigableString):
                if tag.text == "\n":
                    pass
                else:
                    text = tag.text.replace("\n", " ")
                    output.append(re.sub(' +', ' ', text))
            elif isinstance(tag, Tag):
                if tag.name == "para":
                    group = General_XML.parse_component_to_object(tag.contents, directory_path)
                    output.append(group)
                elif tag.name == "figure":
                    output.extend(General_XML.parse_component_to_object(tag.contents, directory_path))
                elif tag.name == "br":
                    pass
                elif tag.name == "graphic":
                    output.append(Graphic(tag, directory_path))
                elif tag.name == "yesno-question":
                    output.extend(General_XML.parse_component_to_object(tag.contents, directory_path))
                elif tag.name == "entity":
                    character_dict = General_XML.get_character_dict()
                    try:
                        character = character_dict[tag.text]
                        output.append(character)
                    except KeyError:
                        Exception(f"Could not find character {tag.text} in the character dictionary")
                elif tag.name == "emphasis":
                    output.append(Emphasis(tag))
                elif tag.name == "list":
                    contents = General_XML.parse_component_to_object(tag.contents, directory_path)
                    output.append(XMLList(tag, contents))
                elif tag.name == "listitem":
                    output.append(General_XML.parse_component_to_object(tag.contents, directory_path))
                elif tag.name == "passage":
                    output.extend(General_XML.parse_component_to_object(tag.contents, directory_path))
                elif tag.name == "span":
                    output.extend(General_XML.parse_component_to_object(tag.contents, directory_path))
                elif tag.name == "urllink":
                    pass
                else:
                    raise Exception(f"Unexpected for tag {tag.name}")
            else:
                raise Exception(f"Unknown tag type {type(tag)}")
        return output
