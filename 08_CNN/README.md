# Convolutional Neural Network Notes

This folder contains the deep learning section of the HackBio teaching notes. The notebooks move from a simple CNN on handwritten digits to biomedical image classification, breast ultrasound segmentation, and DNA motif detection from real ChIP-seq data.

The teaching emphasis is on shapes, tensors, model architecture, training loops, evaluation metrics, and biological interpretation.

## Notebooks

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `01_CNN_with_MNIST.ipynb` | Introductory CNN for handwritten digit classification | PyTorch basics, MNIST loading, convolution, pooling, flattening, training loop, accuracy |
| `02_MED_MNIST.ipynb` | CNN for DermaMNIST skin lesion images | 3-channel medical images, multiclass classification, binary risk grouping, multi-head CNN |
| `busi_unet_segmentation_tutorial.ipynb` | U-Net segmentation of breast ultrasound lesions | Image-mask pairs, encoder-decoder architecture, skip connections, BCE loss, Dice, IoU, prediction overlays |
| `real_chipseq_ctcf_motif_cnn_notebook.ipynb` | 1D CNN for CTCF motif detection from real ChIP-seq peaks | ENCODE data, hg38 FASTA, summit-centered windows, one-hot DNA encoding, Conv1D, AUROC, AUPRC, filter interpretation |

## What Students Should Learn

- How image tensors are shaped as batch, channel, height, and width.
- Why convolutions preserve local structure better than flattened tabular features.
- How pooling reduces spatial dimensions.
- How PyTorch models, losses, optimizers, and training loops fit together.
- How segmentation differs from classification.
- Why Dice and IoU are useful for segmentation.
- How DNA sequences can be represented as one-hot encoded tensors for 1D convolution.
- How learned filters can sometimes be inspected as motif-like patterns.

## Dataset Notes

### MNIST

`01_CNN_with_MNIST.ipynb` downloads MNIST through `torchvision`:

```python
datasets.MNIST(root="data", train=True, download=True, transform=transform)
```

### DermaMNIST

`02_MED_MNIST.ipynb` uses `dermamnist` from MedMNIST:

```python
data_flag = "dermamnist"
```

The notebook creates both a 7-class target and a binary higher-risk target.

### BUSI

`busi_unet_segmentation_tutorial.ipynb` expects a local folder:

```python
DATA_DIR = Path("./BUSI")
```

The expected pattern is image files with matching mask files named like:

```text
image.png
image_mask.png
```

Class subfolders such as benign, malignant, or normal can be kept inside `BUSI/`.

### CTCF ChIP-seq

`real_chipseq_ctcf_motif_cnn_notebook.ipynb` downloads:

- ENCODE CTCF K562 peak file `ENCFF396BZQ`
- UCSC hg38 reference genome FASTA

This notebook may require more time, disk space, and internet access than the smaller image-classification examples.

## Suggested Teaching Flow

1. Start with MNIST to explain convolution, pooling, flattening, and dense layers.
2. Move to DermaMNIST to show medical images and multi-task outputs.
3. Teach U-Net after students understand basic CNN blocks.
4. End with the ChIP-seq notebook to show that CNNs are not only for images; they can also learn sequence patterns.

## Practice Prompts

- Change the number of convolution filters in the MNIST model.
- Compare training and validation accuracy in the DermaMNIST notebook.
- Modify the binary higher-risk class grouping and discuss the biological implications.
- In the BUSI notebook, change the threshold used to convert probabilities into masks.
- Replace BCE loss with BCE plus Dice loss in the segmentation notebook.
- In the ChIP-seq notebook, inspect different first-layer filters and compare their consensus patterns.

## Requirements

Main packages used across this folder:

```bash
pip install numpy pandas matplotlib scikit-learn torch torchvision pillow medmnist pyfaidx logomaker
```

`logomaker` is optional; the ChIP-seq notebook can still run without it, but sequence-logo style plots will be skipped.
