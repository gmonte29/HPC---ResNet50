# HPC---ResNet50
Training a ResNet50 model amongst various CPU/GPU parallelism scenarios

Mac GPU Setup

Setup and activate python enviornment:

  python3 -m venv ~/venv-metal
  source ~/venv-metal/bin/activate
  python -m pip install -U pip

install tensorflow and metal gpu plugin:

  python -m pip install tensorflow
  python -m pip install tensorflow-metal

source: https://developer.apple.com/metal/tensorflow-plugin/


Cluster NVIDIA GPU Setup

In cluster node with GPUs available create and activate Anaconda enviornment:

  CONDA_OVERRIDE_CUDA="11.2" conda create --name tf2-gpu "tensorflow==2.12.1=cuda112*" --channel conda-forge
  conda activate tf2-gpu

source: https://researchcomputing.princeton.edu/support/knowledge-base/tensorflow
