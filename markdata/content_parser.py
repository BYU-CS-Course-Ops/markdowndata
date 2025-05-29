import re
import yaml
from .utils import convert_value


def parse_content_block(text: str):
    text = text.strip()
    if not text:
        return {}

    yaml_match = re.search(r'---\s*\n(.*?)\n---', text, re.DOTALL)
    if yaml_match:
        try:
            yaml_data = yaml.safe_load(yaml_match.group(1))
            if yaml_data:
                return {k: convert_value(v) for k, v in yaml_data.items()}
        except yaml.YAMLError:
            pass

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

    list_items = re.findall(r'^[\-*+]\s+(.*)$', text, re.MULTILINE)
    if list_items:
        return [convert_value(item) for item in list_items]

    return convert_value(text)
