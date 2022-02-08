.. _installation:

Installation
------------
``bioimageloader`` is a Python library. Make sure you have Python and `pip <https://pip.pypa.io/en/stable/>`_ installed.
You can do so through `conda <https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links>`_
, through a package manager that your OS supports, or `<https://www.python.org/>`_.

Option 1
^^^^^^^^
Install ``bioimageloader`` through `<https://pypi.org/>`_

.. code-block:: bash

   pip install bioimageloader


Option 2
^^^^^^^^
or install it directly from source (need git installed)

.. code-block:: bash

   pip install "git+https://github.com/sbinnee/bioimageloader@master"


Option 3
^^^^^^^^
for dev environment, have a editable local copy

.. code-block:: bash

   git clone "https://github.com/sbinnee/bioimageloader"
   cd bioimageloader
   pip install --editable .
