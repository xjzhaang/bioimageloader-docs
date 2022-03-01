More: Split training/test set
=============================
Some datasets (actually many) do not split training/test sets. It is up to us how to
split. We will look at two functions, namely :py:func:`bioimageloader.utils.random_split_dataset`
and :py:func:`bioimageloader.utils.split_dataset_by_indices`.


Random split
------------
Let's pick one dataset which does not provide training/test split, for instance
:py:class:`bioimageloader.collections.ComputationalPathology`. We will split it
into three parts (training/validation/test) using
:py:func:`bioimageloader.utils.random_split_dataset`.

.. code-block:: python
   :linenos:

   import random
   from bioimageloader.collections import ComputationalPathology
   from bioimageloader.utils import random_split_dataset

   # set random seed
   SEED = 42
   random.seed(SEED)
   # load dataset
   dset = ComputationalPathology('./data/ComputationalPathology')

   # define ratios and numbers
   r_train = 0.6
   r_val = 0.2
   #r_test = 0.2  # the rest
   # get real numbers
   n_train = int(r_train * len(dset))
   n_val = int(r_val * len(dset))
   n_test = len(dset) - n_train - n_val

   # SPLIT!
   dset_train, dset_val, dset_test = random_split_dataset(
      dset,
      [n_train, n_val, n_test]
   )
   # these assertions will not throw AssertionError
   assert len(dset_train) == n_train
   assert len(dset_val) == n_val
   assert len(dset_test) == n_test


Manual split
------------
Manual split means hard-coded indices. I found it useful to have hard-coded
indices for training/test split for all datasets and have them saved somewhere
for experiments and analyses. We will use :py:func:`bioimageloader.utils.split_dataset_by_indices`.

.. code-block:: python
   :linenos:

   import random
   from bioimageloader.collections import ComputationalPathology
   from bioimageloader.utils import split_dataset_by_indices

   # set random seed
   SEED = 42
   random.seed(SEED)
   # load dataset
   dset = ComputationalPathology('./data/ComputationalPathology')

   # define ratios and numbers
   r_train = 0.6
   r_val = 0.2
   #r_test = 0.2  # the rest
   # get real numbers
   n_train = int(r_train * len(dset))
   n_val = int(r_val * len(dset))
   n_test = len(dset) - n_train - n_val

   # get indices and save them if you want
   indices = list(range(len(dset)))
   random.shuffle(indices)
   idx_train = [indices.pop() for _ in range(n_train)]
   idx_val = [indices.pop() for _ in range(n_val)]
   idx_test = [indices.pop() for _ in range(n_test)]

   # SPLIT!
   dset_train = split_dataset_by_indices(dset, idx_train)
   dset_val = split_dataset_by_indices(dset, idx_val)
   dset_test = split_dataset_by_indices(dset, idx_test)
   # these assertions will not throw AssertionError
   assert len(dset_train) == n_train
   assert len(dset_val) == n_val
   assert len(dset_test) == n_test
