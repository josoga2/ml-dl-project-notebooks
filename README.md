# Machine Learning and Deep Learning Teaching Notes for HackBio

This repository contains beginner-friendly teaching notebooks that I developed for introducing machine learning and deep learning concepts to HackBio learners through biological, biomedical, and public-health examples. The notebooks move from interpretable classical models to tree ensembles, dimensionality reduction, convolutional neural networks, image segmentation, and genomic sequence modeling.

My goal is not only to run models, but to help learners understand the full modeling workflow: asking a biological question, preparing data, choosing a model, training, evaluating, interpreting results, and thinking about limitations.

## Repository Map

| Order | Folder | Theme | Main notebooks | What learners practice |
| --- | --- | --- | --- | --- |
| 1 | [`01_linear_regression`](01_linear_regression/) | Linear regression | `01_Simple_Linear_Regression.ipynb`, `02_Multivariate_Linear_Regression.ipynb` | Predicting continuous outcomes, train/test split, coefficients, R2, mean squared error |
| 2 | [`02_logistic_regression`](02_logistic_regression/) | Logistic regression and feature selection | `03_Logistic_Regression_Feature_Selection.ipynb` | Binary classification, scaling, feature selection, ROC curves, biological interpretation |
| 3 | [`04_rf`](04_rf/) | Random forests | `04_Random_Forest_Pneumonia.ipynb` | Image classification with a classical ML model, confusion matrices, pixel importance |
| 4 | [`05_xgboost`](05_xgboost/) | Gradient boosting with XGBoost | `05_XGBoost_for_AMR_Text_Classification.ipynb`, `05_Cancer_Metastasis_Prediction.ipynb` | Tabular classification, categorical encoding, boosted trees, feature importance |
| 5 | [`07_dim_red`](07_dim_red/) | Dimensionality reduction | `07_Dimensionality_Reduction_with_PCA_TSNE.ipynb` | High-dimensional data, variance filtering, PCA, t-SNE, visualization of sample structure |
| 6 | [`08_CNN`](08_CNN/) | Deep learning and CNNs | `01_CNN_with_MNIST.ipynb`, `02_MED_MNIST.ipynb`, `busi_unet_segmentation_tutorial.ipynb`, `real_chipseq_ctcf_motif_cnn_notebook.ipynb` | CNNs for images, multi-task learning, U-Net segmentation, 1D CNNs for DNA motif detection |

## Suggested Learning Path

1. Start with linear regression to learn supervised learning in its simplest form.
2. Move to logistic regression to introduce classification and probability.
3. Use random forests to show non-linear models and model interpretation.
4. Use XGBoost to discuss stronger tabular models and feature importance.
5. Introduce PCA and t-SNE before deep learning so learners can reason about high-dimensional biological data.
6. Finish with CNNs, moving from simple image classification to biomedical image segmentation and genomic sequence modeling.

## How to Run the Notebooks

You can run the notebooks locally with JupyterLab, in VS Code, or in a hosted environment such as Google Colab. For local use, create an environment and install the main packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install jupyterlab numpy pandas matplotlib seaborn scikit-learn xgboost medmnist torch torchvision pillow pyfaidx logomaker
jupyter lab
```

Some notebooks download public datasets during execution, so an internet connection is useful. A few notebooks expect local datasets to be placed beside the notebook or in a named data folder; see the module READMEs for details.

## Data Notes

| Notebook area | Data source or requirement |
| --- | --- |
| Linear regression | FEV physiology dataset downloaded from a public GitHub URL |
| Logistic regression | Breast cancer diagnosis dataset downloaded from the HackBio project collection |
| Random forest | PneumoniaMNIST downloaded through `medmnist` |
| XGBoost AMR | Antibiotic resistance tracking dataset downloaded from the HackBio project collection |
| XGBoost cancer and dimensionality reduction | Expects `Breast_GSE45827.csv`; place it in the notebook working directory or adjust the path |
| MNIST CNN | MNIST downloaded through `torchvision` |
| MedMNIST CNN | DermaMNIST downloaded through `medmnist` |
| BUSI U-Net | Expects a local `BUSI/` folder containing ultrasound images and matching mask files |
| ChIP-seq motif CNN | Downloads ENCODE CTCF peaks and the UCSC hg38 reference genome; this can take time and disk space |

## Teaching Focus

These notes are structured for live teaching, self-study, and project-based practice. Each module can be taught as a short standalone lesson, but the full sequence works best as a gradual build-up:

- Models first, then interpretation.
- Small biological examples before high-dimensional omics data.
- Classical machine learning before deep learning.
- Accuracy and confusion matrices before specialized metrics such as Dice, IoU, AUROC, and AUPRC.
- Code execution paired with biological reasoning.

## Suggested Student Workflow

1. Read the problem statement before running code.
2. Run the notebook top to bottom once without edits.
3. Re-run selected cells while changing one parameter at a time.
4. Write down what changed in the result and why it might have changed.
5. End each notebook by explaining the model in plain language.

## Good Extension Questions

- What assumptions does this model make about the data?
- Which preprocessing steps are essential, and which are optional?
- How would the result change with a different train/test split?
- Are the selected features biologically meaningful?
- Which metric best matches the scientific or clinical question?
- What would be needed before using this model outside the classroom?

## Repository Status

This folder is organized as teaching material rather than a packaged Python library. The notebooks are the primary source of instruction, and each topic folder now includes its own README to help students navigate the lesson.

> Some parts of this readme were written with chatGPT. 