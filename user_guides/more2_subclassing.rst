More: Modifying existing collections
====================================
All collections are python class, meaning you can make a subclass out of it in order to
modify default behaviors, or implement new methods and attributes.

Let's say, you would like to use :py:class:`bioimageloader.collections.BBBC007`
dataset to train a U-Net. While ``BBBC007`` does not provide mask annotation,
which U-Net typically requires, it comes with outline annotation that we can
easily convert into mask annotation.

All you have to do is to copy class definition of `BBBC007 source <../_modules/bioimageloader/collections/_bbbc007.html>`_
and to override ``get_mask()`` method. Go to the source link and compare it with
codes below. In summary,

1. Copy class source
2. Change class name to something else
3. Override ``get_mask()`` method
4. (optional) Give new argument(s) and write docs

Below codes use `scipy.ndimage.binary_fill_holes() <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_fill_holes.html>`_
from ``scipy`` package.

.. code-block:: python
   :linenos:

   from pathlib import Path
   from typing import List, Optional, Sequence, Union

   import albumentations
   import numpy as np
   import tifffile

   from bioimageloader.collections import BBBC007
   from bioimageloader.utils import stack_channels

   # ndi.binary_fill_holes() will fill outline annotation
   import scipy.ndimage as ndi


   class BBBC007variant(BBBC007):
       """Drosophila Kc167 cells (VARIANT)

       NU-Net needs outline to be filled and only need DNA annotation.

       Outline annotation

       Images were acquired using a motorized Zeiss Axioplan 2 and a Axiocam MRm
       camera, and are provided courtesy of the laboratory of David Sabatini at the
       Whitehead Institute for Biomedical Research. Each image is roughly 512 x 512
       pixels, with cells roughly 25 pixels in dimeter, and 80 cells per image on
       average. The two channels (DNA and actin) of each image are stored in
       separate gray-scale 8-bit TIFF files.

       Notes
       -----
       - [4, 5, 11, 14, 15] have 3 channels but they are just all gray scale
           images. Extra work is required in get_image().

       .. [1] Jones et al., in the Proceedings of the ICCV Workshop on Computer
          Vision for Biomedical Image Applications (CVBIA), 2005.
       .. [2] [BBBC007](https://bbbc.broadinstitute.org/BBBC007)
       """
       # Dataset's acronym
       acronym = 'BBBC007'

       def __init__(
           self,
           root_dir: str,
           *,
           output: str = 'both',
           transforms: Optional[albumentations.Compose] = None,
           num_calls: Optional[int] = None,
           # specific to this dataset
           image_ch: Sequence[str] = ('DNA', 'actin',),
           anno_ch: Sequence[str] = ('DNA',),
           # arguments for VARIANT
           fill_holes: bool = True,
           **kwargs
       ):
           """
           Parameters
           ----------
           root_dir : str
               Path to root directory
           output : {'image', 'mask', 'both'} (default: 'both')
               Change outputs. 'both' returns {'image': image, 'mask': mask}.
           transforms : albumentations.Compose, optional
               An instance of Compose (albumentations pkg) that defines
               augmentation in sequence.
           num_calls : int, optional
               Useful when ``transforms`` is set. Define the total length of the
               dataset. If it is set, it overwrites ``__len__``.
           image_ch : {'DNA', 'actin'} (default: ('DNA', 'actin'))
               Which channel(s) to load as image. Make sure to give it as a
               Sequence when choose a single channel.
           anno_ch : {'DNA', 'actin'} (default: ('DNA',))
               Which channel(s) to load as annotation. Make sure to give it as a
               Sequence when choose a single channel.
           fill_holes : bool (default: True)
               Fill outline annotation using `scipy.ndimage.binary_fill_holes()`

           See Also
           --------
           BBBC007 : Super class
           MaskDataset : Super class
           DatasetInterface : Interface
           """
           # Pass existing arguments to its super class
           super().__init__(
               root_dir=root_dir,
               output=output,
               transforms=transforms,
               num_calls=num_calls,
               image_ch=image_ch,
               anno_ch=anno_ch,
               **kwargs
           )
           # arguments for VARIANT
           self.fill_holes = fill_holes

       # override
       def get_mask(self, p: Union[Path, List[Path]]) -> np.ndarray:
           if isinstance(p, Path):
               mask = tifffile.imread(p)
           else:
               mask = stack_channels(tifffile.imread, p)
           # VARIANT behavior
           if self.fill_holes:
               mask = ndi.binary_fill_holes(mask)
           # output.dtype=bool and bool is not well handled by albumentations
           return mask.astype(np.float32)
