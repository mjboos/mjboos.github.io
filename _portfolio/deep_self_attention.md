---
title: "Deep auditory encoding with self-attention to predict brain activity"
excerpt: "This Python package allows you to train a recurrent DNN (a GRU) and learn a self-attention mechanism that weighs hidden states."
collection: portfolio
---

[This library](https://github.com/mjboos/selfattention_audio) allows you to train a recurrent DNN (a GRU) and learn a self-attention mechanism that weighs hidden states - the resulting weighted tensor is used to predict brain activity (or whatever you choose as a target).
It also contains many variations of this model type (shared attention between targets, multi-head attention etc) and some functions for visualizing the computed attention weights on a spectrogram.

The general idea is captured in this figure:

<img src="https://mjboos.github.io/images/gru_attention_model.png" alt="attention model" width="800"/>

Read more in [this blogpost](https://mjboos.github.io/Deep-auditory-encoding-models-with-attention/)!
