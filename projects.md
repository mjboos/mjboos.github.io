# Projects

## Deep auditory encoding with self-attention to predict brain activity

[This library](https://github.com/mjboos/selfattention_audio) allows you to train a recurrent DNN (a GRU) and learn a self-attention mechanism that weighs hidden states - the resulting weighted tensor is used to predict brain activity (or whatever you choose as a target).
It also contains many variations of this model type (shared attention between targets, multi-head attention etc) and some functions for visualizing the computed attention weights on a spectrogram.

The general idea is captured in this figure:

<img src="https://mjboos.github.io/images/gru_attention_model.png" alt="attention model" width="800"/>

Read more in [this blogpost](blog/2022/deep-auditory-encoding-attention)!

---

## A BIDS app implementing voxel-wise encoding models in fMRI using Docker

The [voxel-wise encoding BIDS app](https://mjboos.github.io/voxelwiseencoding) is a suite of Python tools for preprocessing fMRI and stimulus data, temporally aligning them, creating a lagged stimulus representation and training and validating voxel-wise encoding models using Ridge regression with hyperparameter search. If you don't want to bother with a full Python installation, or want to run your analyses on a HPC cluster, you can easily use a Docker image for a smooth and reproducible workflow.

<img src='https://raw.githubusercontent.com/mjboos/voxelwiseencoding/master/scheme_BIDS_encoding.png'>

See [this blogpost](blog/2020/voxelwise-encoding-bids.ipynb) to learn more!

---

## Jigsaw Toxic Comment Classification Challenge on Kaggle

This was my first Kaggle challenge that I took seriously and I managed to get into the top 3% (119th place out of 4550 teams) - nothing to brag about, but a great learning experience nonetheless.

You can find the repository with all code for preprocessing the text data, training various models, doing hyperparameter search for various models, doing rigorous cross-validation and creating out-of-sample predictions that can be used for ensembling [here](https://github.com/mjboos/jigsaw).
