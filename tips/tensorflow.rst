TensorFlow installation
-----------------------
This guide is about installing GPU enabled TensorFlow python package on Nvidia
GPU with CUDA capability.

It can be daunting to install TensorFlow with GPU enabled, because official
guide is not much of help and TF requires very strict versions of all its
dependencies (even though not all of them need to be). The most annoying part is
to match Nvidia driver and CUDA toolkit version. As for driver, it should be
fine if it is not too long outdated. As for CUDA toolkit, which takes care of
GPU calculation, **do not install it directly through Nvidia page**. You may
think that the official page is the safest and the most stable way to install
anything. I am not against you and actually `their documentation
<https://developer.nvidia.com/cuda-toolkit-archive>`_ is very thorough how to
install CUDA toolkit on every OS platforms. The truth is, however, they do not
necessarily care about compatibility with a certain version of TensorFlow. If
you still insist to install CUDA toolkit through the official docs, you could
try it and I wish you do not break anything on your system.

What I think the best way is to use ``conda`` through community channel called
``conda-forge`` (https://conda-forge.org). Someone already went through all the pain of
searching for the right combination of dependencies and built tensorflow from the source
and uploaded there. All you have to do is to install it through ``conda``.

Create a new virtual environment using conda and execute ``conda search -c
conda-forge tensorflow-gpu``. You will see multiple packages with different
build tags, such as cuda102py39, etc. "cuda102" means that that pkg was compiled
with CUDA toolkit 10.2 and compatible with python3.9. Choose a right CUDA
toolkit (``cudatoolkit``) version (**WARNING** it is not always the best to use
the latest version. Check compatibility with the driver version and your GPU)
and install it with ``tensorflow-gpu``. ``conda`` already knows your OS and CPU
architecture (when you installed it) and it will auto-detect python version,
already installed pkgs. Accordingly, it will choose the best ``cudatoolkit`` and
``tensorflow-gpu``.

If you do not care about other packages or a specific version of python, you can simply
execute commands below:

.. code-block:: bash

   conda create --name tf-gpu tensorflow-gpu


If you would like to have certain versions of pkgs, you can do something like below:

.. code-block:: bash

   # create virtual env
   conda create --name tf-gpu python=3.9
   # search
   conda search --channel conda-forge cudatoolkit
   conda search --channel conda-forge tensorflow-gpu
   # install cudatoolkit 10.2 and tensorflow-gpu 2.6.x
   conda install --channel conda-forge cudatoolkit=10.2 tensorflow-gpu=2.6

   # or with oneline
   conda create --name py39tf26-gpu --channel conda-forge python=3.9 cudatoolkit=10.2 tensorflow-gpu=2.6


Useful links
^^^^^^^^^^^^
* StarDist Git repository : https://github.com/stardist/stardist
* conda documentation : https://docs.conda.io/en/latest/
* CUDA toolkit documentation : https://developer.nvidia.com/cuda-toolkit-archive
* GPU on Apple M1 : https://forum.image.sc/t/napari-tensorflow-aicsimageio-stardist-care-n2v-pyclesperanto-running-native-on-apple-silicon-m1/55051/3


Useless links 🙃
^^^^^^^^^^^^^^^^
* tensorflow installation docs : https://www.tensorflow.org/install
