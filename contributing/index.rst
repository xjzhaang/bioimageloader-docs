Contributing
============
**Contributions are always welcome!**

**All development is done on Github**: https://github.com/LaboratoryOpticsBiosciences/bioimageloader

- That being said, you need to use ``git`` to make changes.

- If you would like to add a feature, please file an issue first:
https://github.com/LaboratoryOpticsBiosciences/bioimageloader/issues

- If you find a bug and want to fix it, you can directly make a pull request:

   1. Fork the repository
   2. Clone the repository locally
   3. (optional, but recommended) Make a clean virtual environment
   4. Install ``bioimageloader`` in development mode
   5. Make changes, test, and commit them
   6. (if needed) Recompile and update docs. Follow instruction in ``docs/README.md``
   7. Create a pull request: https://github.com/LaboratoryOpticsBiosciences/bioimageloader/pulls


Test
----
Currently ``bioimageloader`` lacks of unit tests. It means you need to manually make
sure that your changes do not break anything, which is not easy without unit tests... So
if you love writing unit tests (does anyone...?), you are more than welcome and your
efforts will be well appreciated!


Code convention
---------------
You can install minimal dev tools with pip. The choices are opinionated. You can totally
ignore them and use whatever suits you, except automatic code formatters.

.. code-block:: bash

   git clone --recurse-submodules https://github.com/LaboratoryOpticsBiosciences/bioimageloader.git
   cd bioimageloader
   pip install --editable .[dev]

I personally do not use automatic code formatter and think that ``bioimageloader`` does
not need one for the moment considering the repo is small, but I may consider one in the
future. Currently, I would like to have some tools to keep codes in consistent shapes.

- [numpydoc](https://numpydoc.readthedocs.io/en/latest/)

   (required) All docs should follow numpydoc syntax and formats

- [mypy](https://github.com/python/mypy)

   (optional) Static type checker. Typing is a good way to find bugs.

- [flake8](https://flake8.pycqa.org/en/latest/)

   (optional) I don't follow all formats it suggests but I do some. The only thing I
   always follow is "Module imported but unused (F401)".

- [isort](https://pycqa.github.io/isort/)

   (optional) Imports can easily become ugly.


Adding a new collection
-----------------------
Collections are the core value of ``bioimageloader``. Thank you for considering
contribution! Please be aware that every collections that ``bioimageloader`` provides
should be public and reachable by all potential users.

After writing a new collection, please follow below steps,

1. Make sure it has docstrings. Place it under the directory ``bioimageloader/collections``.

2. Update ``bioimageloader.collections.__init__`` module

3. Update ``configs/all_collections.yml`` file

4. Run ``docs/_notebooks/_plots.ipynb`` to update histogram in :doc:`../catalogue/index`.
   And sample 2 images (and 2 annotation images, if they exist) place them under
   ``docs/_static/sample_images``. Sample images will be displayed at
   `collection overview table <../_static/table_maskdataset.html>`_, once you compile
   docs.

5. Update ``docs/_static/table_maskdataset.md`` and ``docs/_static/table_maskdataset.html.orig``,
   following ``docs/README.md``

6. Compile docs and check if everything is okay

7. Make a pull request in `both library repo <https://github.com/LaboratoryOpticsBiosciences/bioimageloader>`_
   and `docs repo <https://github.com/LaboratoryOpticsBiosciences/bioimageloader-docs>`_.
