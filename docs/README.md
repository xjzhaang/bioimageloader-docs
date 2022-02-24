# Docs
Compile docs using make and sphinx. Find HTML inside `_build/html/index.html`.

## Notes
- Allow only HTML compilation
- Notebooks in `$ROOT/docs/notebooks` are symbolic links from `$ROOT/notebooks`
- Post compilation
    - `modify_table_html.py`: Add necessary tags to `table_maskdataset.html`
    - `add_images_table_html.py`: Add samples images to `table_maskdataset.html`

Compile docs
``` bash
make html
```

Clean docs
```bash
make clean
```

## How to update table overview
Table is stored in `_static/table_maskdataset.md` as a Markdown format. Once you added a
new dataset, please update this table accordingly. After that go to
https://www.tablesgenerator.com/ and copy and paste the table to convert it into HTML
format. Download and save it in `_static/table_maskdataset.html`.

Make exactly two sample images in PNG format and save them in `_static/sample_images`.
Set filenames following other examples "`{acronym}_{n_sample}_{ind_sample}.png`".
Normally, it should be enough to write acronym in the filename.

This HTML file will be processed as a post-processing step before sphinx-build by
`scripts/add_images_table_html.py`.
