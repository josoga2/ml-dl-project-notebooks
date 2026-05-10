# XGBoost Notes

This folder introduces XGBoost, a powerful gradient boosting method for tabular classification. The examples use biomedical and public-health datasets to show how boosted decision trees can work with structured predictors, categorical variables, and high-dimensional gene expression features.

## Notebooks

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `05_XGBoost_for_AMR_Text_Classification.ipynb` | Predict patient outcome from antimicrobial resistance profiles | Tabular AMR data, label encoding, binary classification, XGBoost model training, ROC AUC |
| `05_Cancer_Metastasis_Prediction.ipynb` | Predict cancer class from gene expression | High-dimensional expression data, label encoding, scaling, variance filtering, `SelectKBest`, multiclass XGBoost, feature importance |

## What Students Should Learn

- Why boosted trees are strong models for structured tabular data.
- How XGBoost builds an ensemble sequentially.
- How to encode categorical variables before modeling.
- How to handle high-dimensional biological data with feature filtering.
- How to read classification reports, confusion matrices, ROC AUC, and feature importance plots.
- Why feature importance is a hypothesis-generating tool rather than final biological proof.

## Dataset Notes

### AMR Outcome Notebook

The AMR notebook downloads data from the HackBio project collection:

```python
amr_source = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/antibiotic_resistance_tracking.csv"
```

It focuses on `ICU` versus `Recovered` outcomes and uses predictors such as age, gender, specimen type, test method, resistance genes, and selected antibiotics.

### Cancer Gene Expression Notebook

The cancer notebook expects a local CSV file:

```python
cm = pd.read_csv("Breast_GSE45827.csv")
```

To run it unchanged, place `Breast_GSE45827.csv` in the notebook working directory, or update the path inside the notebook. The notebook expects columns named `samples` and `type`, with gene or probe measurements used as features.

## Suggested Teaching Flow

1. Introduce gradient boosting as many weak learners combined into a strong model.
2. Start with the AMR notebook because the data is easier to inspect.
3. Discuss categorical encoding and why labels must be numeric for many models.
4. Move to the gene expression notebook to introduce high-dimensional feature spaces.
5. Show how variance filtering and `SelectKBest` reduce the number of predictors.
6. Use feature importance to motivate downstream biological validation.

## Practice Prompts

- Tune `n_estimators`, `max_depth`, or `learning_rate` and observe the effect.
- Compare XGBoost with logistic regression or random forest on a similar task.
- Change the number of selected gene-expression features.
- Discuss why feature importance can be unstable when predictors are correlated.

## Requirements

Main packages used here:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
```
