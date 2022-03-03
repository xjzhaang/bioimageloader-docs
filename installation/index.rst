Installation
============
``bioimageloader`` is a Python library. Make sure you have Python whose version is **3.8
or higher** and `pip <https://pip.pypa.io/en/stable/>`_ installed. You can do so through
`conda <https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links>`_ ,
through a package manager that your OS supports, or `<https://www.python.org/>`_.

Open a terminal where you can execute ``pip`` or ``git`` and choose an option of your
choice.

Option 1
--------
Install ``bioimageloader`` through `<https://pypi.org/>`_

.. code-block:: bash
   :linenos:

   pip install bioimageloader


Option 2
--------
or install it directly from source (need git installed)

.. code-block:: bash
   :linenos:

   pip install "git+https://github.com/LaboratoryOpticsBiosciences/bioimageloader@main"


Option 3
--------
for dev environment, have a editable local copy

.. code-block:: bash
   :linenos:

   git clone "https://github.com/LaboratoryOpticsBiosciences/bioimageloader"
   cd bioimageloader
   pip install --editable .[dev]
