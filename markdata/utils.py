from typing import Union
from dataclasses import dataclass

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt


@dataclass
class Section:
    """
    Represents a single section of the Markdown document.
    Contains its title, header level, location in the original text, and raw content.
    """
    title: str
    level: int
    start: int
    end: int
    content: str


@dataclass
class Node:
    """
    Represents a node in the hierarchical section tree.
    Holds the section title, header level, parsed content, and nested subsections.
    """
    title: str
    level: int
    parsed: Union[dict, list, str]
    subsections: list


def get_md_soup(text: str) -> BeautifulSoup:
    """
    Converts a Markdown text block into HTML and parses it into a BeautifulSoup object.
    """
    md_parser = MarkdownIt().enable("table")  # Enables markdown table parsing
    html = md_parser.render(text)
    return BeautifulSoup(html, 'html.parser')


def convert_value(value: str) -> Union[int, float, str]:
    """
    Convert a string to an int or float is possible, or return the original string.
    """
    value = value.strip()
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except ValueError:
        return value

