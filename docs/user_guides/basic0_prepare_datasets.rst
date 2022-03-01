Basic: Prepare datasets
=======================
Before we get to use ``bioimageloader``, you need dataset(s) to load. ``bioimageloader``
provides collections, but that does not mean that you can download them by using
``bioimageloader``. Links to the papers or to the project pages are provided. We believe
that it is important for you to go there, read papers, understand terms and licenses
before using their works, because bioimages themselves are results of paramount time,
efforts, and resources.


1. Browse and download supported collections
--------------------------------------------
You can browse supported collections with their description and links at :ref:`Collection
Catalogue` and `collection overview table <../_static/table_maskdataset.html>`_. Choose
one or more datasets and download them on your local machine.

Optionally, if you have a set of images, you might want to try out
:py:func:`bioimageloader.utils.get_dataset_from_directory` or
:py:func:`bioimageloader.utils.get_maskdataset_from_directory` depending on the
structure of your dataset. Read more following the links to each function above. **Note
that these functions are experimental**.


2. Unzip it
-----------
There are in large 4 different structures when it comes to an archive file. To explain
each, let's name a zip file **dataset.zip**. It may seem subtle and trivial but bare
with me, because ``bioimageloader`` works with root directories of datasets and
therefore it is important to define what the root directory is. We will call root
directory ``root_dir`` as it is an argument required for all the collections in
``bioimageloader``.

**The rule of thumb is to have a project directory that contains all related contents to
a dataset.**


1. Zipped contents

   You may have encountered this case before, that you unzipped an archive in your
   working directory and found all the contents mingled and mixed with other files.
   Nobody wants that. We want them in a new directory, for instance, ``dataset/``
   (trailing slash means it is a directory) following the name of the archive. Make one
   and unzip contents inside it. Then root directory becomes ``dataset/``, a.k.a.
   ``root_dir=dataset``.

   .. code-block:: bash

      dataset.zip/
         content0.jpg
         content1.jpg
         content2.jpg


2. Zipped a directory

   We appreciate those who suffered and prevented the case that we saw above. In this
   case, the root directory simply becomes ``root_dir=dataset``. We **still want to make
   a new directory** though, because ``image/`` does not match the name of the archive
   and is too generic to distinguish from others when mixed. In the end, it will have
   structure of ``dataset/image/*.jpg``.

   .. code-block:: bash

      dataset.zip/
         image/
            content0.jpg
            content1.jpg
            content2.jpg

   What if the name of archive and that of the directory inside are the same, such as
   below? We do not need a new directory, since it was the intention to avoid case 1
   that we saw. Instead of having a redundant subdirectory of the same name
   ``dataset/dataset/*.jpg``, we have ``dataset/*.jpg``

   .. code-block:: bash

      dataset.zip/
         dataset/
            content0.jpg
            content1.jpg
            content2.jpg

   If there are any contents beside a directory such as below, even though the main
   directory has the same name as the archive itself, we want a new directory to keep
   the all contents as intended. You should have contents under
   ``dataset/dataset/*.jpg`` with ``root_dir=dataset``.

   .. code-block:: bash

      dataset.zip/
         README
         LICENSE
         dataset/
            content0.jpg
            content1.jpg
            content2.jpg


3. Zipped the whole project

   Same as the last example in case 2. Some datasets may come with codes for processing
   steps or etc (we can guess that this type of archives was a part of supplimentary
   materials attached under a report/paper). Notice that the one below is not zipped
   with a root directory just like case 1. Make a new directory ``dataset/``, unzip the
   archive, and the root directory becomes ``root_dir=dataset``, not ``dataset/data``!

   .. code-block:: bash

      dataset.zip/
         code/
         data/
            image/
               content0.jpg
               content1.jpg
               content2.jpg
         README


4. Comes with multiple archives or metadata

   So far through 1 to 3, it assumed that one dataset comes within a single archive
   file. Sometimes, however, a dataset comes with multiple archive files or with
   separate metadata. This is true for most datasets from BBBC (`Broad Bioimage
   Benchmark Collection <https://bbbc.broadinstitute.org/>`_). For example, `BBBC007
   <https://bbbc.broadinstitute.org/BBBC007>`_ comes with two archive files and `BBBC015
   <https://bbbc.broadinstitute.org/BBBC015>`_ with a zip file for images and metadata
   in .xls and .txt formats. So we cannot apply the above logic, that is *zip archive ==
   root directory*.

   Instead, we want to unzip all archives in a directory (``root_dir=BBBC007``), such as
   below:

   .. code-block:: bash

      BBBC007/
         BBBC007_v1_images/
         BBBC007_v1_outlines/

   For BBBC015:

   .. code-block:: bash

      BBBC015/
         BBBC015_v1_images/
         BBBC015_v1_platemap.xls
         BBBC015_v1_platemap.txt


We hope that decisions above look resonable to you. To be honest, some implementations
might not have followed the rules above. If you found such cases, try to point
``root_dir`` to one directory above or below and so on, and please file an issue through
github repository https://github.com/sbinnee/bioimageloader/issues.
