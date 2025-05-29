from typing import Union, List, IO
from .section_tree import split_sections, build_section_tree
from .utils import Node

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
        self.data = self._build_dict_from_tree(structured_tree)
        return self.data

    def _build_dict_from_tree(self, sections: List[Node]) -> dict:
        result = {}
        for node in sections:
            sub_dict = self._build_dict_from_tree(node.subsections)
            if isinstance(node.parsed, dict):
                merged = {**node.parsed, **sub_dict}
            elif node.parsed or sub_dict:
                merged = node.parsed if node.parsed else sub_dict
            else:
                merged = node.parsed
            result[node.title] = merged
        return result
