---
title: "A BIDS app implementing voxel-wise encoding models in fMRI using Docker "
excerpt: "Do you have a BIDS-compliant dataset and stimulus and want to train and validate voxel-wise encoding models in a reproducible workflow? Using this BIDS app, this is as easy as writing a single line in your terminal."
collection: portfolio
---

The [voxel-wise encoding BIDS app](https://github.com/mjboos/voxelwiseencoding) is a suite of Python tools for preprocessing fMRI and stimulus data, temporally aligning them, creating a lagged stimulus representation and training and validating voxel-wise encoding models using Ridge regression with hyperparameter search. If you don't want to bother with a full Python installation, or want to run your analyses on a HPC cluster, you can easily use a Docker image for a smooth and reproducible workflow.
