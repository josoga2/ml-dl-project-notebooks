# Random Forest Notes

This folder introduces random forest classification with a biomedical image example. The notebook uses PneumoniaMNIST, a small chest X-ray dataset from MedMNIST, and trains a classical machine learning model on flattened image pixels.

The lesson is useful for showing that image data can be modeled even before introducing deep learning, while also making clear why CNNs are usually better suited to images.

## Notebook

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `04_Random_Forest_Pneumonia.ipynb` | Classify normal versus pneumonia chest X-rays | MedMNIST loading, image visualization, flattening pixels, random forest training, classification report, confusion matrix, pixel importance heatmap |

## What Students Should Learn

- What an ensemble model is.
- How random forests combine many decision trees.
- How image pixels can be converted into tabular features.
- Why flattening images loses spatial structure.
- How to evaluate a classifier with accuracy, a classification report, and a confusion matrix.
- How feature importance can be reshaped into a rough pixel-level heatmap.

## Dataset

The notebook downloads PneumoniaMNIST through `medmnist`:

```python
from medmnist import PneumoniaMNIST

train_ds = PneumoniaMNIST(split="train", download=True)
val_ds = PneumoniaMNIST(split="val", download=True)
test_ds = PneumoniaMNIST(split="test", download=True)
```

The task is binary classification:

- `0` = normal
- `1` = pneumonia

## Suggested Teaching Flow

1. Show a few example X-ray images and labels.
2. Explain why scikit-learn expects a 2D feature matrix.
3. Flatten each 28 x 28 image into a 784-length vector.
4. Train the random forest and inspect predictions.
5. Discuss the confusion matrix.
6. Reshape feature importances back into 28 x 28 pixels and discuss what that visualization can and cannot prove.

## Practice Prompts

- Change the number of trees with `n_estimators` and compare performance.
- Try using validation data during model selection.
- Compare the random forest approach with the CNN notebooks in `08_CNN`.
- Ask whether the important pixels correspond to clinically meaningful regions.

## Requirements

Main packages used here:

```bash
pip install numpy matplotlib scikit-learn medmnist
```
