from typing import Union
from dataclasses import dataclass


@dataclass
class Section:
    title: str
    level: int
    start: int
    end: int
    content: str


@dataclass
class Node:
    title: str
    level: int
    parsed: Union[dict, list, str]
    subsections: list


def convert_value(value: str) -> Union[int, float, str]:
    value = value.strip()
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value