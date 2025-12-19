# Deep Learning for Signals and Images  
**Reconstruction, Classification, and Model Evaluation under Realistic Constraints**

## Overview

This repository contains two deep learning projects developed as part of an advanced module on signal and image modeling.  
Both projects emphasize **rigorous model design, evaluation, and debugging**, with direct relevance to **quantitative finance**, where similar challenges arise in signal extraction, forecasting, and risk modeling.

The projects focus on:
- learning structured mappings between high-dimensional inputs and targets
- handling noisy, imbalanced, and constrained data
- balancing model complexity against generalization
- metric-driven validation and diagnostics

---

## Project 1 — Cross-Modal Image Translation with Dense U-Net

### Problem Setting

Given paired samples:

$$
x_i \in \mathbb{R}^{H \times W}, \quad y_i \in \mathbb{R}^{H \times W}
$$

the goal is to learn a nonlinear mapping:

$$
f_\theta : x \mapsto y
$$

by minimizing a pixel-wise reconstruction loss:

$$
\mathcal{L}(\theta) = \frac{1}{N} \sum_{i=1}^N \ell\big(f_\theta(x_i), y_i\big)
$$

This task is conceptually analogous to:
- signal denoising
- conditional expectation estimation
- feature-to-target regression

### Model Architecture

A **Dense U-Net–style convolutional network** is implemented, combining:
- encoder–decoder structure (multi-scale representations)
- dense blocks with feature reuse (improved gradient flow)
- skip connections to preserve fine spatial structure

Key design choices:
- dense blocks mitigate vanishing gradients
- fully convolutional (input-size agnostic)
- deliberately constrained capacity (~550k parameters) to control overfitting

This mirrors the **bias–variance trade-off** common in quantitative modeling.

### Data Preprocessing

- Winsorization at the 1st–99th percentiles
- Min–max normalization to $[0,1]$
- Identical preprocessing for training and validation sets

This was critical to stabilize optimization and avoid domination by extreme values.

### Training and Evaluation

- Optimizer: Adam
- Loss: MSE (with MAE / SSIM explored)
- Learning-rate scheduling via ReduceLROnPlateau
- Diagnostic: single-batch overfitting test

Metrics:
- MAE (robust absolute error)
- PSNR (log-scaled reconstruction fidelity)
- qualitative visual inspection

Representative results:
- **MAE ≈ 0.05**
- **PSNR ≈ 20 dB**

---

## Project 2 — ECG Beat Classification with 1D CNNs and Attention

### Problem Setting

The second project addresses **ECG heartbeat classification**, a noisy time-series problem with:
- strong class imbalance (normal vs abnormal beats)
- variable-length signals
- high sensitivity to local temporal patterns

This setup closely resembles:
- anomaly detection
- rare-event modeling
- imbalanced classification in finance

### Data Representation

- Beats filtered to physiologically plausible durations
- Zero-padded to a fixed length (256 samples)
- Represented as 1D signals suitable for convolutional models

### Models Implemented

1. **Baseline 1D CNN**
   - Two convolutional layers
   - Max-pooling and batch normalization
   - Fully connected MLP head

2. **1D CNN + Multi-Head Attention**
   - Self-attention applied to convolutional feature maps
   - Attention-weighted representations before classification

3. *(Exploratory)* CNN–LSTM hybrids (found ineffective for this task)

### Training Strategy

- WeightedRandomSampler to mitigate class imbalance
- Macro-F1 prioritised over accuracy
- Binary evaluation: normal vs abnormal beats
- Strict separation of training and validation pipelines

### Evaluation Metrics

Multiclass:
- Accuracy
- Precision (macro)
- Recall (macro)
- Macro F1

Binary (normal vs abnormal):
- Accuracy
- Precision
- Recall
- Specificity
- F1

### Key Findings

- The **simple 1D CNN outperformed more complex attention-based models**
- Local temporal features dominate ECG beat discrimination
- Attention increased complexity without improving generalisation
- Class imbalance primarily reduced precision for minority classes

---

## Quantitative Finance Relevance

Across both projects, this work demonstrates:

- translating abstract objectives into trainable models
- handling noisy, high-dimensional signals
- principled bias–variance trade-offs
- robust metric-driven evaluation
- disciplined experimentation and debugging

These skills directly transfer to:
- signal extraction and filtering
- forecasting under noise
- anomaly detection
- model validation and stress testing
- research-style experimental workflows

---

## Repository Structure

- `Assessment_Q1.ipynb` — Dense U-Net cross-modal reconstruction
- `Assessment_Q2.ipynb` — ECG classification with CNNs and attention
- `References.md` — External resources and AI usage declaration
- `README.md` — Project overview

---

## Tech Stack

- Python, PyTorch
- NumPy, Matplotlib
- scikit-learn
- Weights & Biases
- GPU-accelerated training

---

## Notes on Academic Integrity

All code, experiments, and explanations were independently designed and verified.  
External resources and AI tools were used strictly for **learning and clarification**, and are fully documented in `References.md`.

---

*This repository is intended as a research-style portfolio project demonstrating applied deep learning for signals and images, with emphasis on rigor, evaluation, and transferability to quantitative domains.*

---

## Author
MSc student Francesco Giuseppe Remondi, Imperial College London  
(Repository cloned from original coursework submission for portfolio purposes.)
