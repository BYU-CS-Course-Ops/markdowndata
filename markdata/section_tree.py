import re
import yaml
from typing import List, Union

from utils import Section, Node, convert_value


def split_sections(text: str) -> List[Section]:
    pattern = re.compile(r'^(?P<header>#+) (?P<title>[^\n]+)', re.MULTILINE)
    matches = list(pattern.finditer(text))

    sections = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append(
            Section(
                title=match.group('title').strip(),
                level=len(match.group('header')),
                start=match.start(),
                end=end,
                content=text[match.end():end].strip()
            )
        )
    return sections


def build_section_tree(flat_sections: List[Section]) -> List[dict]:
    root = Node(
        title='Root',
        level=0,
        parsed={},
        subsections=[]
    )
    stack = [root]

    for section in flat_sections:
        node = Node(
            title=section.title,
            level=section.level,
            parsed=parse_content_block(section.content),
            subsections=[]
        )

        # Pop stack until we find the correct parent
        while stack and stack[-1]['level'] >= section.level:
            stack.pop()

        # Add to parent's subsections
        stack[-1]['subsections'].append(node)
        stack.append(node)

    return root['subsections']


def parse_content_block(text: str) -> Union[dict, list, str]:
    text = text.strip()
    if not text:
        return {}

    # Parse YAML
    yaml_match = re.search(r'---\s*\n(.*?)\n---', text, re.DOTALL)
    if yaml_match:
        try:
            yaml_data = yaml.safe_load(yaml_match.group(1))
            if yaml_data:
                return {k: convert_value(v) for k, v in yaml_data.items()}
        except yaml.YAMLError:
            pass

    # Parse Table
    table_lines = [line.strip() for line in text.split('\n') if '|' in line]
    if table_lines:
        header = [h.strip() for h in table_lines[0].strip('|').split('|')]
        table_data = []
        for row in table_lines[2:]:
            values = [convert_value(v.strip()) for v in row.strip('|').split('|')]
            if len(values) == len(header):
                table_data.append(dict(zip(header, values)))
        if table_data:
            return table_data

    # Parse List
    list_items = re.findall(r'^[\-*+]\s+(.*)$', text, re.MULTILINE)
    if list_items:
        return [convert_value(item) for item in list_items]

    # Fallback Text
    return convert_value(text)
