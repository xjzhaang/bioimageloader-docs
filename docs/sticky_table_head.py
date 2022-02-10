"""Make header of table sticky

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

    # Find head
    for n_open, line in enumerate(lines):
        if re.search(r'<thead>', line):
            break
    for n_open, line in enumerate(lines[n_open:], n_open):
        if re.search(r'<tr>', line):
            break
    print(n_open, line)
    n = line.find('<tr>')
    lines[n_open] = line[:n] + '<tr style="position:sticky; top:0; background-color:#999">\n'
    print(n_open, lines[n_open])

    with open(F_TABLE, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    print(PROG)
    main()
