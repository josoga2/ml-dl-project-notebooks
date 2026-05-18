# Convolutional Neural Network Notes

This folder contains the deep learning section of the HackBio teaching notes. The notebooks move from a simple CNN on handwritten digits to biomedical image classification, breast ultrasound segmentation, and DNA motif detection from real ChIP-seq data.

The teaching emphasis is on shapes, tensors, model architecture, training loops, evaluation metrics, and biological interpretation.

## Notebooks

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `01_CNN_with_MNIST.ipynb` | Introductory CNN for handwritten digit classification | PyTorch basics, MNIST loading, convolution, pooling, flattening, training loop, accuracy |
| `02_MED_MNIST.ipynb` | CNN for DermaMNIST skin lesion images | 3-channel medical images, multiclass classification, binary risk grouping, multi-head CNN |
| `brats_unet_copy.ipynb` | U-Net segmentation of brain tumors from multi-modal MRI | Multi-modal MRI (T1, T1ice, T2, FLAIR), H5 format, encoder-decoder architecture, skip connections, binary tumor mask, BCE loss |
| `real_chipseq_ctcf_motif_cnn_notebook.ipynb` | 1D CNN for CTCF motif detection from real ChIP-seq peaks | ENCODE data, hg38 FASTA, summit-centered windows, one-hot DNA encoding, Conv1D, AUROC, AUPRC, filter interpretation |

## What Students Should Learn

- How image tensors are shaped as batch, channel, height, and width.
- Why convolutions preserve local structure better than flattened tabular features.
- How pooling reduces spatial dimensions.
- How PyTorch models, losses, optimizers, and training loops fit together.
- How segmentation differs from classification.
- Why multi-modal medical imaging (e.g., different MRI sequences) provides complementary information for diagnosis.
- How encoder-decoder architectures with skip connections (U-Net) enable precise localization in segmentation tasks.
- How to work with H5 formatted data commonly found in medical imaging datasets.
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

### BRATS

`brats_unet_copy.ipynb` downloads BraTS2020 training data from Kaggle:

```python
import kagglehub
path = kagglehub.dataset_download(
    "awsaf49/brats2020-training-data",
    output_dir = "/mnt/volume/datasets"
)
```

The dataset contains multi-modal MRI images (T1, T1ice, T2, FLAIR) stored in H5 format. Each file contains:
- `image`: 4-channel array (240 × 240 × 4) with the four MRI modalities
- `mask`: 3-channel array (240 × 240 × 3) with tumor region labels

The notebook extracts the FLAIR modality and creates a binary tumor mask by summing across mask channels.

### CTCF ChIP-seq

`real_chipseq_ctcf_motif_cnn_notebook.ipynb` downloads:

- ENCODE CTCF K562 peak file `ENCFF396BZQ`
- UCSC hg38 reference genome FASTA

This notebook may require more time, disk space, and internet access than the smaller image-classification examples.

## Suggested Teaching Flow

1. Start with MNIST to explain convolution, pooling, flattening, and dense layers.
2. Move to DermaMNIST to show medical images and multi-task outputs.
3. Teach U-Net after students understand basic CNN blocks.
4. Use BRATS to show U-Net on multi-modal medical imaging (brain tumor segmentation) before the ChIP-seq notebook.
5. End with the ChIP-seq notebook to show that CNNs are not only for images; they can also learn sequence patterns.

## Practice Prompts

- Change the number of convolution filters in the MNIST model.
- Compare training and validation accuracy in the DermaMNIST notebook.
- Modify the binary higher-risk class grouping and discuss the biological implications.
- In the BRATS notebook, experiment with different MRI modalities beyond FLAIR (e.g., T1, T2).
- In the BRATS notebook, modify the tumor mask aggregation and threshold for multi-class segmentation.
- Visualize learned U-Net encoder filters in the BRATS notebook to see what the network learns about tumor boundaries.
- In the ChIP-seq notebook, inspect different first-layer filters and compare their consensus patterns.

## Requirements

Main packages used across this folder:

```bash
pip install numpy pandas matplotlib scikit-learn torch torchvision pillow medmnist pyfaidx logomaker h5py kagglehub
```

- `h5py` and `kagglehub` are required for the BRATS notebook to load and download the BraTS2020 dataset.
- `logomaker` is optional; the ChIP-seq notebook can still run without it, but sequence-logo style plots will be skipped.
