"""Make header of table sticky and add footer

Table is generated from .md file through https://www.tablesgenerator.com/
"""

import sys
import re
import warnings

PROG = sys.argv[0]
F_TABLE = '../_static/table_maskdataset.html'


def main():
    with open(F_TABLE) as f:
        lines = f.readlines()
    for line in lines:
        if re.search(r"position:sticky", line):
            warnings.warn(f"{F_TABLE}: Already have sticky head")
            return

    # #--- Sticky head ---# #
    for n_open, line in enumerate(lines):
        if re.search(r'<thead>', line):
            break
    for n_open, line in enumerate(lines[n_open:], n_open):
        if re.search(r'<tr>', line):
            break
    n = line.find('<tr>')
    lines[n_open] = line[:n] + '<tr style="position:sticky; top:0; background-color:#999">\n'

    # #--- Anchor links---# #
    # from <td class="tg-0pky">[DSB2018](https://www.kaggle.com/c/data-science-bowl-2018)</td>
    # into <td class="tg-0pky"><a href="https://www.kaggle.com/c/data-science-bowl-2018"><span style="color:#905">[DSB2018](https://www.kaggle.com/c/data-science-bowl-2018)</span></a></td>
    # from <td class="tg-0pky">[${1}](${2})</td>
    # into <td class="tg-0pky"><a href="${2}"><span style="color:#905">[${1}](${2})</span></a></td>
    for i, line in enumerate(lines):
        r = re.search(r'https?://\S+\)', line)
        if r:
            link = r.group()[:-1]
            _, k = r.span()
            link = r.group()[:-1]

            td = re.search(r'<td class="tg-0pky">', line)
            _, j = td.span()

            new_line = line[:j] + f'<a href="{link}"><span style="color:#905">' + line[j:k] + '</span></a>' + line[k:]
            lines[i] = new_line

    # #--- Footer ---# #
    footer = """<footer>Annotation
        * ●: Either sementic or instance
        * ▲: Partially segmented (either semantic or instance)
        * B: Biological labels
        * C: Counts
        * F: Foreground/background
        * O: Outlines of objects
        * U: Bounding boxes
        </footer>"""
    lines.extend([footer])

    with open(F_TABLE, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    print(PROG)
    main()
