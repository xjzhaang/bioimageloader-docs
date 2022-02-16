More: Writing a custom Dataset
==================================
Process of making a new custom dataset is similar to that of PyTorch. Relevant
classes are :py:class:`bioimageloader.base.DatasetInterface`, :py:class:`bioimageloader.base.Dataset`,
and :py:class:`bioimageloader.base.MaskDataset`. Each class has its own
requirements.

Abstract class ``bioimageloader.base.DatasetInterface`` defines a basic
structure of every dataset classes implemented in ``bioimageloader``. You **DO
NOT** want to make a subclass inherited directly from it.

Instead, you may want to make your subclass based on ``bioimageloader.base.Dataset``
or on ``bioimageloader.base.MaskDataset`` (more to come). As you might have
guessed, class ``MaskDataset`` is a base for all datasets that have mask
annotation. Class ``Dataset`` is a base for those that do not have any
annotation available as well as a super class for ``MaskDataset``. In short, if
your dataset you would like to implement has mask annotation, then do
subclassing from ``MaskDataset``, otherwise do from ``Dataset``.

There is an example template `template.py
<https://github.com/sbinnee/bioimageloader/tree/main/bioimageloader/template.py>`_
in the git repository. The best practice is to read source codes of existing
collections and to see how they are implemented.

You are always welcome to file an issue through `Github repository <https://github.com/sbinnee/bioimageloader/issues>`_
if you need any help.
