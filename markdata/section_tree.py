import re
from .utils import Section, Node
from .content_parser import parse_content_block


def split_sections(text: str):
    pattern = re.compile(r'^(?P<header>#+) (?P<title>[^\n]+)', re.MULTILINE)
    matches = list(pattern.finditer(text))

    sections = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append(Section(
            title=match.group('title').strip(),
            level=len(match.group('header')),
            start=match.start(),
            end=end,
            content=text[match.end():end].strip()
        ))
    return sections


def build_section_tree(flat_sections):
    root = Node(title='Root', level=0, parsed={}, subsections=[])
    stack = [root]

    for section in flat_sections:
        node = Node(title=section.title, level=section.level,
                    parsed=parse_content_block(section.content), subsections=[])

        while stack and stack[-1].level >= section.level:
            stack.pop()
        last_node = stack[-1]
        last_node.subsections.append(node)
        stack.append(node)

    return root.subsections
