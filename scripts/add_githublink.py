import os.path
import glob
import re
import sys

PROG = os.path.basename(sys.argv[0])
GITHUB_LINK = "https://github.com/sbinnee/bioimageloader"
EXCLUDE = [
    'table_maskdataset.html',
    'hist_mask_collections_div.html',
    'hist_all_collections_div.html'
]


def put_logo(html):
    # #--- Read html ---# #
    with open(html) as f:
        lines = f.readlines()
    for line in lines:
        if re.search(f"Added by {PROG}", line):
            # warnings.warn(f"{html}: Logo and link already added")
            return
    # #--- Sidebar ---# #
    # find '<div class="sidebar-logo-container">'
    # find '<div class="sidebar-brand">'
    for n_open, line in enumerate(lines):
        if re.search(r'<a class="sidebar-brand"', line):
            break
    #print(n_open, line)

    for n_close, line in enumerate(lines[n_open:], n_open):
        if re.search(r'</a>', line):
            break
    #print(n_close, line)

    # make space
    line = lines.pop(n_close)
    i_start = line.find('</a>')
    lines.insert(n_close, line[i_start:i_start+4] + '\n')
    lines.insert(n_close+1, line[i_start+4:])

    logo_sidebar = """<!-- Added by add_githublink.py -->
      <a class="sidebar-brand reference" href="{}" style="justify-content: center; align-items: center;">
        <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
          <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
        </svg>Github
      </a>
    """.format(GITHUB_LINK)
    lines.insert(n_close, logo_sidebar)
    #print("Add logo in Sidebar")

    # #--- Footer ---# #
    # find Show Source
    for n_open, line in enumerate(lines):
        if re.search(r'Show Source', line):
            break
    #print(n_open, line)

    for n_close, line in enumerate(lines[n_open:], n_open):
        if re.search(r'</a>', line):
            break
    #print(n_close, line)

    logo_footer = """<!-- Added by add_githublink.py -->
              | <a href="{}">
                <svg height="14" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
                  <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                </svg>Github repo
              </a>
    """.format(GITHUB_LINK)
    lines.insert(n_close + 1, logo_footer)
    #print("Add logo in Footer")

    # #--- Write ---# #
    with open(html, 'w') as f:
        f.writelines(lines)


def main():
    print('Link:', GITHUB_LINK)

    htmls = glob.glob('_build/html/**/*.html', recursive=True)
    if len(htmls) == 0:
        raise FileNotFoundError("No html found")
    for html in htmls:
        base = os.path.basename(html)
        if base in EXCLUDE:
            continue
        put_logo(html)
    print("Put github logo and a link to git repo")


if __name__ == '__main__':
    main()
