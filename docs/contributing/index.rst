Contributing
============
Contributions are always welcome!

All development is done on Github: https://github.com/sbinnee/bioimageloader

That being said, you need to use ``git`` to make changes.

If you would like to add a feature, please file an issue first:
https://github.com/sbinnee/bioimageloader/issues

If you find a bug and want to fix it, you can directly make a pull request:

1. Fork the repository
2. Clone the repository locally
3. (optional, but recommended) Make a clean virtual environment
4. Install ``bioimageloader`` in development mode
5. Make changes, test, and commit them
6. Create a pull request: https://github.com/sbinnee/bioimageloader/pulls


Test
----
Currently ``bioimageloader`` lacks of unit tests. It means you need to manually make
sure that your changes do not break anything, which is not possible without unit
tests... So if you love writing unit tests, you are more than welcome and your efforts
will be well appreciated!


Code convention
---------------
You can install minimal dev tools with pip. The choices are opinionated.

I personally do not use automatic code formatter and think that ``bioimageloader`` does
not need one for the moment considering the repo is small, but I am against it. And I
would like to have some tools to keep codes in consistent shapes.

- mypy

   Static type checker. Typing is a good way to find bugs.

- flake8

   I don't follow all formats it suggests but I do some.

- isort

   Imports can easily become ugly.

- numpydoc

   All docs should follow its syntax and formats.


.. code-block:: bash

   cd bioimageloader
   pip install --editable .[dev]
