"""Make header of table sticky and add footer

Table is generated from .md file through https://www.tablesgenerator.com/
"""

import sys
import re
from pathlib import Path
from typing import List, TypeVar
# import warnings

T = TypeVar('T')

PROG = sys.argv[0]
F_TABLE = '_static/table_maskdataset.html'


def search_n_line(lines: List[str], pat: str, scan_from: int = 0) -> int:
    """

    `scan_from` does not scan_from return integer. It is just for efficiency.

    """
    for n, line in enumerate(lines[scan_from:], scan_from):
        if re.search(pat, line):
            return n
    return -1


def insert_lines(lines: List[T], new_lines: List[T], n_line) -> int:
    for i, f in enumerate(new_lines):
        lines.insert(n_line + i, f)
    return len(new_lines)


def main():
    with open(F_TABLE) as f:
        lines = f.readlines()
    for line in lines:
        if re.search(r'<th class="\S+">Image</th>', line):
            # warnings.warn(f"{F_TABLE}: Already have Image field")
            return
    for line in lines:
        if res := re.search(r'<th class="\S+">', line):
            cls = res.group()
            break

    # #--- head ---# #
    n_start_tbody = search_n_line(lines, r'<thead>')
    n_end_tbody = search_n_line(lines, r'</tr>', scan_from=n_start_tbody)
    new_fields = [f'    {cls}Image</th>\n',
                  f'    {cls}Annotation</th>\n']
    offset = insert_lines(lines, new_fields, n_line=n_end_tbody)
    # print(lines[n_end_tbody-1:n_end_tbody+4])

    # #--- body ---# #
    n_tbody = search_n_line(lines, r'<tbody>', scan_from=n_end_tbody+offset)
    lst_acronym = []
    lst_n_tr = []
    for n_tr, line in enumerate(lines[n_tbody:], n_tbody):
        if re.search(r'<tr>', line):
            # print(n_tr, lines[n_tr+1])
            acronym = re.search(r'>\S+<', lines[n_tr+1]).group()[1:-1]
            lst_acronym.append(acronym)
            lst_n_tr.append(n_tr)

    for acronym in lst_acronym:
        n_acronym = search_n_line(lines, acronym, n_tbody)
        imgs = sorted(Path('./_static/sample_images').glob(f'{acronym}*image*'))
        annos = sorted(Path('./_static/sample_images').glob(f'{acronym}*annotation*'))
        img_tags = [
            f'    {cls}<img src="{imgs[0].relative_to("./_static")}" alt="image0" height=256px>\n',
            # f'    <td class="tg-0pky"><img src="{imgs[0].relative_to("./_static")}" alt="image0" height=256px>\n',
            f'                        <img src="{imgs[1].relative_to("./_static")}" alt="image1" height=256px></td>\n'
        ]
        n_tr_end = search_n_line(lines, r'</tr>', n_acronym)
        offset = insert_lines(lines, img_tags, n_tr_end)
        if annos:
            anno_tags = [
                f'    {cls}<img src="{annos[0].relative_to("./_static")}" alt="annotation0" height=256px>\n',
                # f'    <td class="tg-0pky"><img src="{annos[0].relative_to("./_static")}" alt="annotation0" height=256px>\n',
                f'                        <img src="{annos[1].relative_to("./_static")}" alt="annotation1" height=256px></td>\n'
            ]
            insert_lines(lines, anno_tags, n_tr_end + offset)

    with open(F_TABLE, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    print("Put images and annotations in the html table")
    main()
