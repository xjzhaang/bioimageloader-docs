Basic: Load multiple datasets
=============================
Load multiple datasets either one by one or use :py:class:`bioimageloader.Config` to
read them all at once from ``.yml`` file. If you are not familiar with yaml format
please, check out `<https://quickref.me/yaml>`_ or go to the `official yaml webpage
<https://yaml.org/>`_ for more detail.


Concatenate multiple datasets
-----------------------------
Grouping multiple datasets allows to load them as if they are a single dataset. You can
define ``transforms`` for each dataset and group them together. Concatenating can be
done by wrapping them in list with :py:class:`bioimageloader.ConcatDataset`.

Note that every datasets concatenated within the same group should have the same output
keys. For example, you cannot mix a dataset that only returns 'image' with another one
that returns both 'image' and 'mask'. Be aware that some datasets do not offer
annotation, meaning that those do not have ``output`` parameter.


.. code-block:: python
   :linenos:

   import albumentations as A
   from bioimageloader.collections import DSB2018, TNBC, BBBC016
   from bioimageloader import ConcatDataset, BatchDataloader

   # transforms for each dset
   transforms_dsb2018 = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.HorizontalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.2),
   ])
   transforms_tnbc = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.VerticalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.4),
   ])
   transforms_bbbc016 = A.Compose([
       A.RandomSizedCrop(min_max_height=[300, 500], width=256, height=256),
       A.Blur(p=0.5),
       A.RandomBrightnessContrast(p=0.6),
   ])
   # construct dsets
   dsb2018 = DSB2018('./data/DSB2018', output='image', transforms=transforms_dsb2018)
   tnbc = TNBC('./data/TNBC_NucleiSegmentation', output='image', transforms=transforms_tnbc)
   bbbc016 = BBBC016('./data/BBBC016_v1', transforms=transforms_bbbc016)  # do not have annotation
   # concatenate
   cat = ConcatDataset([dsb2018, tnbc, bbbc016])
   # load them in batch
   call_cat = BatchDataloader(cat,
                              batch_size=16,
                              drop_last=True,
                              num_workers=8)
   # iterate transformed images
   for meow in call_cat:
       image = meow['image']
       # these assertions will not throw AssertionError
       assert image.shape[0] == 16
       assert image.shape[1] == 256 and image.shape[2] == 256
       do_something(image)



Load datasets using ``config.yml``
----------------------------------
You can make a yaml file to manage parameters for multiple datasets in one place.

``./config/config.yml``

.. code-block:: yaml
   :linenos:

   DSB2018:
     root_dir: ./data/DSB2018/
     output: image
   TNBC:
     root_dir: ./data/TNBC_NucleiSegmentation/
     output: image
   BBBC016:
     root_dir: ./data/BBBC016_v1/


``./main.py``

.. code-block:: python
   :linenos:

   import albumentations as A
   from bioimageloader import Config

   # parse config
   config = Config('./config/config.yml')

   # 1. load datsets without transforms
   datasets: list[Dataset] = config.load_datasets()
   print([dset.acronym for dset in datsets])
   # ['DSB2018', 'TNBC', 'BBBC016']

   # 2. load datasets with the same transforms for all datasets
   transforms = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.HorizontalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.2),
   ])
   datasets_transformed = config.load_datasets(transforms)

   # 3. load datsets with a set of transforms for each dataset
   transforms_dsb2018 = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.HorizontalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.2),
   ])
   transforms_tnbc = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.VerticalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.4),
   ])
   transforms_bbbc016 = A.Compose([
       A.RandomSizedCrop(min_max_height=[300, 500], width=256, height=256),
       A.Blur(p=0.5),
       A.RandomBrightnessContrast(p=0.6),
   ])
   # organize all in a dictionary
   transforms_indv: dict = {
       'DSB2018': transforms_dsb2018,
       'TNBC': transforms_tnbc,
       'BBBC016': transforms_bbbc016,
   }
   datasets_transformed_indv = config.load_datasets(transforms_indv)
