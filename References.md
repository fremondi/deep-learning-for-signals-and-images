# Coursework - References

This file lists external resources I used for background understanding, debugging, or implementation guidance.

## Q1

### Papers / Articles
- Deep Learning Based Multi-Modal Fusion for Fast MR Reconstruction (Dense-UNet paper): <https://pmc.ncbi.nlm.nih.gov/articles/PMC6541541/#S2>
  - Used for: architectural inspiration (dense blocks, translation layers), hyperparameter choices (growth rate, block depth).

### Documentation
- PyTorch documentation (modules, optimizers, loss functions): https://pytorch.org/docs/stable/index.html
  - Used for: nn.Module patterns, Conv2d/ConvTranspose2d usage, training loop structure.

### Metrics
- PSNR definition reference (Wikipedia): <https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio>
  - Used for: correct PSNR computation for data in [0,1].

### Debugging and Hyperparameter Tuning
- <https://convolution-solver.ybouane.com/>
  - Used for: checking convolution shapes.
- <https://wandb.ai/site/>
  - Used for: tracking hyperparameters and models architectures.

### AI Tools (ChatGPT)

- ChatGPT (OpenAI), used during development for conceptual clarification and debugging guidance.
- Topics discussed included:
  - DenseBlock growth rate and channel concatenation
  - Role of translation layers in Dense-UNet architectures
  - Interpretation of PSNR and MAE in image reconstruction
  - Diagnosing overfitting via training/validation curves
- The tool was used strictly for learning and understanding purposes.
- All implementation decisions, experimental design, and written explanations were independently produced and verified by running experiments and inspecting outputs.
- No text or code was copied from AI outputs.


## Q2

### Dataset / Metadata
- Hugging Face ECG dataset repository:  
  https://huggingface.co/datasets/dpelacani/ecg-led2-cleaned  
  - Used for: loading ECG signals, beat locations, and class labels; understanding dataset structure and class mapping.

### Documentation
- Hugging Face Datasets documentation:  
  https://huggingface.co/docs/datasets/  
  - Used for: dataset loading and handling dataset fields.
- PyTorch documentation:  
  https://pytorch.org/docs/stable/index.html  
  - Used for: implementing 1D CNN architectures, training loops, `WeightedRandomSampler`, and loss functions.
- scikit-learn model evaluation metrics:  
  https://scikit-learn.org/stable/modules/model_evaluation.html  
  - Used for: computing accuracy, precision, recall, macro-F1, specificity, and confusion matrices.

### Papers / Background Reading
- Deep Learning Models for Arrhythmia Classification Using Stacked Time–Frequency Scalogram Images from ECG Signals <https://arxiv.org/pdf/2312.09426> 
  - Used for: architectural inspiration for the baseline CNN model and motivation for comparing CNNs against more complex attention-based architectures.

### Debugging and Experiment Tracking
- Convolution shape calculator:  
  https://convolution-solver.ybouane.com/  
  - Used for: validating convolution and pooling output dimensions in 1D CNNs.
- Weights & Biases:  
  https://wandb.ai/site/  
  - Used for: logging training and validation metrics and comparing model variants.

### AI Tools (ChatGPT)
- ChatGPT (OpenAI) was used during development for conceptual clarification and debugging support.
- Topics discussed included:
  - Handling variable-length ECG beats via filtering and fixed-length padding
  - Strategies for mitigating class imbalance (weighted sampling, metric selection)
  - Implementing evaluation metrics including specificity
  - Interpreting training/validation curves and dimished results from attention models
- The tool was used strictly for learning, research, and understanding purposes.
- All code, experimental design, and written explanations were independently produced and verified through experimentation.
- No text or code was copied verbatim from AI outputs.