# Completing a Full Data Analysis in Python

---

## Defining and Stating Questions or Hypotheses

- **Identify the key questions or hypotheses** you want to answer or test with your analysis.
- Formulate clear, specific, and measurable questions.
- Say what your Data Source is.
- State your questions or hypotheses that your analysis will address.

|||

Example:
- What factors influence customer satisfaction in the bookshop?
- Does the number of staff correlate with the number of books borrowed?

---

## Importing Libraries

- Import the necessary libraries for data analysis and visualization.
- Common libraries include `pandas`, `numpy`, `matplotlib`, and `seaborn`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## Reading the Data

- Read the data into a pandas DataFrame.
- Use functions like `pd.read_csv()`, `pd.read_excel()`, or `pd.read_sql()`.

```python
data = pd.read_csv('bookshop.csv')
```

---

## Initial Data Inspection

- Use methods like `head()`, `tail()`, or `sample()` to get a quick look at the data.
- This helps to understand the structure and content of the data.

```python
data.head()
data.tail()
data.sample(5)
```

---

## Checking for Null Values and Data Types

- Use `info()` to check for null values and data types.
- This helps identify any data cleaning steps needed.

```python
data.info()   
```

---

## Descriptive Statistics

- Use `describe()` to get a summary of the central tendency, dispersion, and shape of dataset distribution.
- This provides insights into the data’s statistical properties.

```python
data.describe()
data.describe(include = "O") #stats on non-numerical columns
```

---

## Data Cleaning

- Handle missing values, incorrect data types, and outliers.
- Techniques include filling missing values, converting data types, and removing or correcting outliers.

```python
# Example: Fill missing values
data['column_name'].fillna(data['column_name'].mean(), inplace=True)
```

---

## Data Visualization

|||

### Histograms and Boxplots

- Visualize the distribution of numerical data.
- Use `hist()` for histograms and `boxplot()` for boxplots.

```python
data['column_name'].hist()
plt.show()

sns.boxplot(x=data['column_name'])
plt.show()
```

|||

### Scatter Plots and Pair Plots

- Explore relationships between variables.
- Use `scatter()` for scatter plots and `pairplot()` for pair plots.
- Note: Only use pair plots on a subset of columns to avoid long processing times.

```python
plt.scatter(data['column_x'], data['column_y'])
plt.show()

# Subset example for pair plot
subset_data = data[['column1', 'column2', 'column3']]
sns.pairplot(subset_data)
plt.show()

|||

### Correlation Matrices and Heat Maps

- Identify correlations between variables.
- Use `corr()` to compute the correlation matrix and `heatmap()` to visualize it.

```python
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
```

---

## Annotating Your Analysis

- Include annotations throughout the notebook to explain your thinking and decisions.
- This helps others understand your analysis process and conclusions.

```markdown
# Example Annotation
# The following scatter plot shows the relationship between the number of staff and the number of books borrowed.
```

---

## Summarizing the Analysis

- Summarize the key findings from your analysis.
- Discuss any patterns, trends, or relationships discovered.
- Highlight any limitations or potential biases in the analysis.

```markdown
# Summary of Analysis
# - There is a positive correlation between the number of staff and the number of books borrowed.
# - The data shows seasonal trends in customer visits.
# - Some limitations include missing data and potential measurement errors.
```

---

## Future Analysis

- Suggest areas for further investigation or analysis.
- Identify any new questions or hypotheses that emerged from the analysis.

```markdown
# Future Analysis
# - Explore customer satisfaction data to identify key drivers.
# - Conduct a time series analysis to forecast future book borrowings.
# - Analyze the impact of marketing campaigns on customer visits.
```

---

## Now: Conduct a Full Data Analysis

- See an example of a complete data analysis [here](https://www.kaggle.com/code/hasibalmuzdadid/ramen-ratings-analysis/notebook).
- Use this framework to conduct a thorough and effective data analysis on a dataset we have looked at previously like the bookshop data.
- Conduct a full data analysis on a new dataset you have identified from Kaggle.com or another source.