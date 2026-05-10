# Linear Regression Notes

This folder introduces supervised learning through linear regression. The examples use the FEV dataset, a physiology dataset where the target is forced expiratory volume, a continuous measure of lung function.

The teaching aim is to help learners understand how a model can estimate a numeric outcome from one or more predictors, and how to interpret fitted coefficients and regression metrics.

## Notebooks

| Notebook | Focus | Main ideas |
| --- | --- | --- |
| `01_Simple_Linear_Regression.ipynb` | Predict FEV from height | One predictor, scatter plots, train/test split, fitted regression line, R2, mean squared error |
| `02_Multivariate_Linear_Regression.ipynb` | Predict FEV from age, height, gender, and smoking status | Multiple predictors, encoding categorical variables, coefficient interpretation, model evaluation |

## What Students Should Learn

- The difference between features (`X`) and target (`y`).
- Why regression is used for continuous outcomes.
- How train/test splitting helps estimate performance on unseen data.
- What the intercept and coefficients mean.
- How to read R2 and mean squared error.
- Why adding more predictors can help, but also requires more careful interpretation.

## Dataset

Both notebooks download the FEV dataset from a public URL:

```python
fev_source = "https://raw.githubusercontent.com/GTPB/PSLS20/master/data/fev.txt"
```

The dataset includes variables such as FEV, age, height, gender, and smoking status.

## Suggested Teaching Flow

1. Start with a scatter plot of height versus FEV.
2. Ask students what kind of line would best summarize the relationship.
3. Fit a simple linear regression model.
4. Interpret the slope in plain language.
5. Move to multiple regression and compare the model behavior.
6. Discuss why biological variables can be correlated with one another.

## Practice Prompts

- Replace height with age in the simple regression notebook. Does the model improve or worsen?
- Compare the simple and multivariate models using R2 and mean squared error.
- Explain the smoking coefficient carefully. What does it mean, and what does it not prove?
- Add a residual plot and discuss whether the model errors look random.

## Requirements

Main packages used here:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
