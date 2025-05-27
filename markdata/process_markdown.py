import re
from typing import Union, List, Dict, IO


class MarkDataParser:
    def __init__(self):
        self.data = {}

    def load(self, file: Union[str, IO]) -> Dict[str, Union[Dict, List[Dict]]]:
        """
        Loads Markdown content from a file path or file-like object and returns parsed structured data.

        :param file: File path as string or an open file object.
        :return: Nested dictionary of extracted tables organized by H1 and H2 sections.
        """
        if isinstance(file, str):
            with open(file, 'r', encoding='utf-8') as f:
                md_text = f.read()
        else:
            md_text = file.read()

        self.data = self._read_md_tables(md_text)
        return self.data

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Splits the Markdown text into H1 sections based on break tags."""
        return [s.strip() for s in re.split(r'(?=^# )', text, flags=re.MULTILINE) if s.strip()]

    @staticmethod
    def _extract_table(lines: List[str]) -> Union[Dict[str, str], List[Dict[str, str]]]:
        """
        Extracts table data from Markdown format.

        :param lines: Lines containing the Markdown table.
        :return: Single dictionary if one row, otherwise list of dictionaries.
        """
        headers = [h.strip() for h in lines[0].split('|')[1:-1]]
        rows = [
            dict(zip(headers, [v.strip() for v in line.split('|')[1:-1]]))
            for line in lines[2:] if line.strip()
        ]
        return rows[0] if len(rows) == 1 else rows

    def _parse_h1_section(self, h1_section: str) -> (str, Dict):
        """
        Parses an H1 section and extracts its H2 subsections and tables.

        :param h1_section: Text of one H1 section.
        :return: Tuple of section title and its data dictionary.
        """
        lines = h1_section.split('\n')
        section_title = lines[0].replace('# ', '').strip()
        section_data = {}
        current_table, tables = [], []
        current_h2, h2_data = None, {}

        for line in lines[1:]:
            if line.startswith('## '):
                if current_h2 and current_table:
                    section_data[current_h2] = self._extract_table(current_table)
                    current_table = []
                current_h2 = line.replace('## ', '').strip()

            elif '|' in line:
                current_table.append(line)

            elif not line.strip() and current_table:
                if current_h2:
                    section_data[current_h2] = self._extract_table(current_table)
                else:
                    tables.append(current_table)
                current_table = []

        if current_table:
            if current_h2:
                section_data[current_h2] = self._extract_table(current_table)
            else:
                tables.append(current_table)

        for table in tables:
            section_data.update(self._extract_table(table))

        return section_title, section_data

    def _read_md_tables(self, md_text: str) -> Dict[str, Union[Dict, List[Dict]]]:
        """Extracts tables and structured data from Markdown text."""
        return dict(self._parse_h1_section(section) for section in self._tokenize(md_text))
