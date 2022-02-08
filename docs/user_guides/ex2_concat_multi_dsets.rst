Example2: Concatenate multiple datasets
---------------------------------------
.. code-block:: python

   from bioimageloader.collections import DSB2018, TNBC, BBBC008
   from bioimageloader.batch import ConcatDataset

   dsb2018 = DSB2018('./data/DSB2018')
   tnbc = TNBC('./data/TNBC_NucleiSegmentation')
   bbbc008 = BBBC008('./data/BBBC008_v1')
