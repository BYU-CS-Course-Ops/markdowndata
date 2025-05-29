import re
import yaml
from typing import Union, List, IO

from section_tree import split_sections, build_section_tree


class MarkDataParser:
    def __init__(self):
        self.data = {}

    def load(self, file: Union[str, IO]) -> dict:
        if isinstance(file, str):
            with open(file, 'r') as f:
                text = f.read()
        else:
            text = file.read()
        flat_sections = split_sections(text)
        structured_tree = build_section_tree(flat_sections)
        self.data = self._build_nested_dict(structured_tree)
        return self.data

    def _build_nested_dict(self, sections: List[dict]) -> dict:
        result = {}
        for section in sections:
            sub_dict = self._build_nested_dict(section['subsections'])
            if isinstance(section['parsed'], dict):
                merged = {**section['parsed'], **sub_dict}
            elif section['parsed'] or sub_dict:
                merged = section['parsed'] if section['parsed'] else sub_dict
            else:
                merged = section['parsed']
            result[section['title']] = merged
        return result
