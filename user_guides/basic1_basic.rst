Basic: Basic usage
==================
This guide will cover basic usage of ``bioimageloader``. Examples down below will load a
dataset from :py:mod:`bioimageloader.collections`, and transform images with a image
augmentation library called `albumentations <https://albumentations.ai/>`_.
Additionally, how to load them with multi-processing, when you need a computationally
heavy set of augmentations.


Load a dataset from collections
-------------------------------
Let's load :py:class:`bioimageloader.collections.DSB2018` (*2018 Data Science Bowl*)
dataset for instance. Output from the iteration is a dictionary of strings as keys and
numpy array as values. You can control the output type through ``output`` parameter.

.. code-block:: python
   :linenos:

   from bioimageloader.collections import DSB2018

   dsb2018 = DSB2018('./data/DSB2018')

   # iterate
   data: dict[str, numpy.ndarray]
   for data in dsb2018:
       image = data['image']
       mask = data['mask']
       do_something(image, mask)


Data augmentation with albumentations
-------------------------------------
Use ``transforms`` keyword argument. Below example defines a set of random crop,
horizontal flip, and random contrast image augmentations. Check out `A list of
transforms and their supported targets
<https://albumentations.ai/docs/getting_started/transforms_and_targets/>`_ from
albumentations library.

Applying transformations often implies random shuffling and you may want to sample more
from datasets. Once you pass ``num_samples``, it will automatically perform shuffle and
set the sampling number to ``num_samples``.

.. code-block:: python
   :linenos:

   import albumentations as A
   from bioimageloader.collections import DSB2018

   transforms = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.HorizontalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.2),
   ])
   num_samples = 2000  # DSB2018 training set has 670 images

   dsb2018 = DSB2018('./data/DSB2018', transforms=transforms, num_samples=num_samples)

   # iterate transformed images
   data: dict[str, numpy.ndarray]
   for data in dsb2018:
       image = data['image']
       mask = data['mask']
       # these assertions will not throw AssertionError
       assert image.shape[0] == 256 and image.shape[1] == 256
       assert mask.shape[0] == 256 and mask.shape[1] == 256
       do_something(image, mask)


Batch loading with multi-processing
-----------------------------------
Batch loading is essential especially when you have a set of augmentations that requires
heavy computation, or when you would like to run deep neural network models which can
benefit from GPU.

Wrap a dataset with :py:class:`bioimageloader.BatchDataloader` and specify a batch size
as well as number of processes.


.. code-block:: python
   :linenos:

   import albumentations as A
   from bioimageloader.collections import DSB2018
   from bioimageloader import BatchDataloader

   heavy_transforms = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.HorizontalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.2),
   ])
   # construct dset with transforms
   dsb2018 = DSB2018('./data/DSB2018', transforms=heavy_transforms)
   batch_loader = BatchDataloader(dsb2018,
                                  batch_size=16,
                                  drop_last=True,
                                  num_workers=8)
   # iterate transformed images
   data: dict[str, numpy.ndarray]
   for data in dsb2018:
       image = data['image']
       mask = data['mask']
       # these assertions will not throw AssertionError
       assert image.shape[0] == 16 and mask.shape[0] == 16
       assert image.shape[1] == 256 and image.shape[2] == 256
       assert mask.shape[1] == 256 and mask.shape[2] == 256
       do_something(image, mask)
