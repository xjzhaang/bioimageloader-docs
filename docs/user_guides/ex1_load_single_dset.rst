Basic usage
===========
This guide will cover basic usage of ``bioimageloader``. Examples down below will load
a datset from ``bioimageloader.collections``, and transform images with a image
augmentation library called `albumentations <https://albumentations.ai/>_`.
Additionally, how to load them with multi-processing, when you need a computationally
heavy set of augmentations.


Load a dataset from collections
-------------------------------
Load DSB2018 (*2018 Data Science Bowl*) dataset for instance

.. code-block:: python

   from bioimageloader.collections import DSB2018

   dsb2018 = DSB2018('./data/DSB2018')

   # iterate
   for data in dsb2018:
      image = data['image']
      mask = data['mask']
      do_something(image, mask)



Data augmentation with albumentations
-------------------------------------
Define a set of random crop, horizontal flip, and random contrast image augmentations.

.. code-block:: python

   import albumentations as A
   from bioimageloader.collections import DSB2018

   transforms = A.Compose([
      A.RandomCrop(width=256, height=256),
      A.HorizontalFlip(p=0.5),
      A.RandomBrightnessContrast(p=0.2),
   ])

   dsb2018 = DSB2018('./data/DSB2018', transforms=transforms)

   # iterate transformed images
   for data in dsb2018:
      image = data['image']
      mask = data['mask']
      # these assertion will not throw AssertionError
      assert image.shape[0] == 256 and image.shape[1] == 256
      assert mask.shape[0] == 256 and mask.shape[1] == 256
      do_something(image, mask)


Batch loading with multi-processing
-----------------------------------

.. code-block:: python

   import albumentations as A
   from bioimageloader.collections import DSB2018
   from bioimageloader import BatchDataloader

   heavy_transforms = A.Compose([
      A.RandomCrop(width=256, height=256),
      A.HorizontalFlip(p=0.5),
      A.RandomBrightnessContrast(p=0.2),
   ])

   dsb2018 = DSB2018('./data/DSB2018', transforms=heavy_transforms)
   batch_loader = BatchDataloader(dsb2018,
                                  batch_size=16,
                                  drop_last=True,
                                  num_workers=8)

   # iterate transformed images
   for data in dsb2018:
      image = data['image']
      mask = data['mask']
      # these assertion will not throw AssertionError
      assert image.shape[0] == 16 and mask.shape[0] == 16
      assert image.shape[1] == 256 and image.shape[2] == 256
      assert mask.shape[1] == 256 and mask.shape[2] == 256
      do_something(image, mask)
