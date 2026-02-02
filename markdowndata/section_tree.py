import re
from .utils import Section, Node
from .content_parser import parse_content_block


def split_sections(text: str):
    """
    Splits the Markdown text into Section objects.
    Each section is identified by a header (e.g., #, ##, ###).
    """
    pattern = re.compile(r'^(?P<header>#+) (?P<title>[^\n]+)', re.MULTILINE)
    code_spans = [match.span() for match in re.finditer(r'```.*?```', text, re.DOTALL)]

    def is_in_code_block(pos: int) -> bool:
        for start, end in code_spans:
            if start <= pos < end:
                return True
        return False

    matches = [match for match in pattern.finditer(text) if not is_in_code_block(match.start())]

    sections = []

    # First grab anything before the initial header
    end = matches[0].start() if matches else len(text)
    sections.append(Section(
        title="",  # The section's title text
        level=0,  # The number of # symbols indicates nesting level
        start=0,  # Position where this header starts in the text
        end=end,  # Position where this section's content ends
        content=text[:end].strip()  # The actual text content of this section (excluding header)
    ))

    for i, match in enumerate(matches):
        # Calculate the 'end' of the current section:
        # It's the start of the next header or the end of the document.
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        sections.append(Section(
            title=match.group('title').strip(),    # The section's title text
            level=len(match.group('header')),      # The number of # symbols indicates nesting level
            start=match.start(),                   # Position where this header starts in the text
            end=end,                               # Position where this section's content ends
            content=text[match.end():end].strip()  # The actual text content of this section (excluding header)
        ))

    return sections


def build_section_tree(sections):
    """
    Builds a hierarchical tree of Nodes from the list of Section objects.
    Uses a stack to track the current section hierarchy.
    """
    root = Node(title='Root', level=0, parsed={}, subsections=[])

    # If the initial section is level 0, it makes part of the root
    if sections[0].level == 0:
        root.parsed = parse_content_block(sections[0].content)
        sections.pop(0)

    stack = [root]

    for section in sections:
        node = Node(
            title=section.title,
            level=section.level,
            parsed=parse_content_block(section.content),
            subsections=[]
        )

        # Find the correct parent in the hierarchy
        while stack and stack[-1].level >= section.level:
            stack.pop()

        # Add this node as a child of the current parent
        parent_node = stack[-1]
        parent_node.subsections.append(node)

        # Push this node to the stack (might have its own children)
        stack.append(node)

    return [root]
