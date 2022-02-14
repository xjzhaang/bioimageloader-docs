# Docs
Compile docs using make and sphinx. Find html inside `_build/html/index.html`.

## Notes
- You cannot compile docs in Windows
- Allow only html compilation
- Notebooks in `$ROOT/docs/notebooks` are symbolic links from `$ROOT/notebooks`
- Post compilation
    - `add_githublink.py`: Put github log and link to repo in every html pages
    - `modify_table_html.py`: Add necessary tags to `table_maskdataset.html`

Compile docs
``` bash
make html
```

Clean docs
```bash
make clean
```
