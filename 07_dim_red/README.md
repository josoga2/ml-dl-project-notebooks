# Dimensionality Reduction Notes

This floder introduces dimensionality reduction for high-dimensional biological data. The notebook uses gene expression data to teach the curse of dimensionality, variance filtering, PCA, and t-SNE.

The main teaching goal is to help learners see how thousands of features can be compressed into fewer dimensions for visualization and exploratory analysis.

## Notebook

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `07_Dimensionality_Reduction_with_PCA_TSNE.ipynb` | Visualize high-dimensional gene expression data | Curse of dimensionality, scaling, variance filtering, PCA explained variance, PC1/PC2 plots, t-SNE projection |

## What Students Should Learn

- Why high-dimensional biological data can be difficult to model and visualize.
- Why filtering low-variance features can simplify analysis.
- How PCA finds directions of maximal variance.
- How to interpret cumulative explained variance.
- Why t-SNE is useful for visualization but not a simple replacement for PCA.
- Why visualization should be interpreted carefully and not treated as proof of biological separation.

## Dataset

The notebook expects a local CSV file:

```python
gexp = pd.read_csv("Breast_GSE45827.csv")
```

To run it unchanged, place `Breast_GSE45827.csv` in the notebook working directory, or update the path inside the notebook. The notebook expects:

- `samples`: sample identifiers
- `type`: sample labels or classes
- remaining columns: gene/probe expression features

## Suggested Teaching Flow

1. Explain the curse of dimensionality with a simple intuition: many features make distance and visualization harder.
2. Load the gene expression matrix and inspect its shape.
3. Scale or filter features before dimensionality reduction.
4. Run PCA and plot cumulative explained variance.
5. Visualize PC1 versus PC2 colored by sample type.
6. Run t-SNE on PCA-reduced features and compare the plot with PCA.

## Practice Prompts

- Change the variance filtering threshold and observe how many features remain.
- Change the number of PCA components.
- Try different t-SNE perplexity values and compare the plots.
- Explain why different t-SNE runs can look different.
- Discuss whether clusters in a 2D plot are enough to make a biological conclusion.

## Requirements

Main packages used here:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
