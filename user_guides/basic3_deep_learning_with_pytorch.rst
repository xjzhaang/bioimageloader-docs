Basic: Deep learning with PyTorch
=================================
If you followed through the guide, you may have noticed that ``bioimageloader`` has many
classes whose interfaces are similar to those of `PyTorch <https://pytorch.org/>`_, a
popular python library for deep learning. It is true that ``bioimageloader`` followed
the design of PyTorch's data module, and especially so for :py:class:`bioimageloader.ConcatDataset`
and :py:class:`bioimageloader.BatchDataloader`. The benefit is that all ``bioimageloader``
datasets are compatible with PyTorch.

For example, you can replace :py:class:`bioimageloader.BatchDataloader` with its
equivalent `DataLoader <https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader>`_
from PyTorch, while keeping the same transformation API from albumentations. In fact,
``albumentations`` is a part of the `PyTorch ecosystem <https://pytorch.org/ecosystem/>`_

Note that you may want to convert image arrays to Tensor which PyTorch can handle, using
`ToTensorV2 <https://albumentations.ai/docs/api_reference/pytorch/transforms/#albumentations.pytorch.transforms.ToTensorV2>`_
from albumentations library. Find a full example guide `here <https://albumentations.ai/docs/examples/pytorch_classification/>`_.


.. code-block:: python
   :linenos:

   import albumentations as A
   from albumentations.pytorch import ToTensorV2  # PyTorch helper
   from bioimageloader.collections import DSB2018
   from torch.utils.data import DataLoader  # PyTorch

   transforms_totensor = A.Compose([
       A.RandomCrop(width=256, height=256),
       A.HorizontalFlip(p=0.5),
       A.RandomBrightnessContrast(p=0.2),
       ToTensorV2(),  # convert numpy ndarray to torch Tensor
   ])
   # construct dset with transforms
   dsb2018 = DSB2018('./data/DSB2018', transforms=transforms_totensor)
   batch_loader = Dataloader(dsb2018,
                             batch_size=16,
                             drop_last=True,
                             num_workers=8)
   # iterate transformed images
   data: dict[str, numpy.ndarray]
   for data in dsb2018:
       image = data['image']  # torch.Tensor, (b, c, h, w)
       mask = data['mask']  # torch.Tensor, (b, h, w)
       # these assertions will not throw AssertionError
       assert image.shape[0] == 16 and mask.shape[0] == 16
       assert image.shape[1] == 3  # notice Tensor convention shape (b, c, h, w)
       assert image.shape[2] == 256 and image.shape[3] == 256
       assert mask.shape[1] == 256 and mask.shape[2] == 256
       do_something(image, mask)
