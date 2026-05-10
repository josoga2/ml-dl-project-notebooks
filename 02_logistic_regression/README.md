# Logistic Regression and Feature Selection Notes

This folder introduces binary classification with logistic regression using a breast cancer diagnosis example. The notebook shows how to predict whether a tumor is malignant or benign from cell nucleus measurements, then connects model features back to biological interpretation.

## Notebook

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `03_Logistic_Regression_Feature_Selection.ipynb` | Predict breast cancer diagnosis | Binary labels, scaling, baseline logistic regression, feature selection, L1 regularization, confusion matrix, ROC curve, AUC |

## What Students Should Learn

- Why logistic regression is used for classification rather than continuous prediction.
- How to encode a binary target, such as malignant versus benign.
- Why feature scaling matters for logistic regression.
- How to compare a model trained on all predictors with a model trained on selected predictors.
- How `SelectKBest` and L1 regularization can identify useful features.
- How to interpret accuracy, precision, recall, confusion matrices, ROC curves, and AUC.

## Dataset

The notebook downloads a breast cancer diagnosis dataset from the HackBio project collection:

```python
bc_source = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv"
```

The target column is `diagnosis`, mapped as:

- `M` -> malignant
- `B` -> benign

## Suggested Teaching Flow

1. Frame the task as a binary classification problem.
2. Inspect the class balance before modeling.
3. Train a baseline model using all predictors.
4. Select a smaller feature set and compare performance.
5. Introduce L1 regularization as automatic feature selection.
6. Use the selected features to discuss biological meaning and model limitations.

## Practice Prompts

- Change the number of selected features from `k=5` to another value and compare results.
- Compare selected features from `SelectKBest` with features selected by L1 regularization.
- Explain why a high accuracy score may not be enough for biomedical classification.
- Identify which errors would be more concerning: false benign or false malignant predictions.

## Requirements

Main packages used here:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
