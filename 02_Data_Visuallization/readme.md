# **Data Visualization:**

<img src="https://img.shields.io/badge/Data%20Analysis:-Python | Numpy | Pandas | Sklearn |-8e2de2?style=for-the-badge" alt="Data Visualization Tools Badge"/>

<img src="https://img.shields.io/badge/Data%20Visualization:-Matplotlib | Seaborn | Plotly |-8e2de2?style=for-the-badge" alt="Data Visualization Tools Badge"/>

## **Overview:**
This project aims to do Exploratory Data Analysis on some popular real-world datasets and create insightful visualizations using Python and libraries like Metplotlib, Seaborn, Plotly, Numpy, Pandas and others.

This project is designed to provide a hands-on experience in data visualization, allowing users to gain insights from various datasets and present them in a visually appealing manner.

> So, the main aim is to do detailed analysis on different datasets with heavy visuallizations.

I utilize Matplotlib, Seaborn, and Plotly to create a range of static and interactive plots that help in understanding and analyzing data effectively.

## **Tools Used:**
- **Python**: The programming language used for data analysis, manipulation and visualization.

- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations in Python.

- **Seaborn**: A statistical data visualization library based on Matplotlib that provides a high-level interface for drawing attractive and informative graphics.

- **Plotly**: An interactive graphing library that makes it easy to create web-based visualizations.

- **Numpy**: A library for numerical computing in Python.

- **Pandas**: A library for data manipulation and analysis.

## **Installation:**
To set up this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/rajesh-coventry/Projects/tree/master/02_Data_Visuallization
   ```

2. Install the required libraries:

    ```bash
    pip install numpy pandas matplotlib seaborn plotly scikit-learn
    ```

## **Possible Plots:**
This project includes a variety of plots, such as:

1. `Line Plots`: Visualize trends over time.

2. `Bar Charts`: Compare different categories.

3. `Histograms`: Show the distribution of a dataset.

4. `Box Plots`: Display the spread and identify outliers.

5. `Scatter Plots`: Explore relationships between two variables.

6. `Heatmaps`: Visualize matrix-like data.

7. `Pie Charts`: Show proportions of categories.

8. `Interactive Plots`: Create engaging visualizations using Plotly.

9. and many more. 

## **Important Dependecies:**

```python
import os
import sys
import warnings
from datetime import datetime
# os, sys: for file paths or custom module access.
# warnings: to suppress or manage warnings.
# datetime: useful for time-based data or tracking execution.

# ------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline  # Ensures plots appear in the notebook
sns.set_theme(style="whitegrid")  # Sets plot theme

# -------------------------------------------------------------------------------------

# plotly.express: high-level API for quick visualizations.
#plotly.graph_objects: for detailed, customized interactive plots.
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------------------------------------------------------------------

warnings.filterwarnings("ignore") # Ignore warnings

# ----------------------------------------------------------------------------------------
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.float_format', lambda x: '%.2f' % x)  # Format floats nicely

# --------------------------------------------------------------------------------------

from IPython.display import display, HTML, Markdown
# display(): for displaying DataFrames, HTML, Markdown, or Plotly figures without needing print.
# HTML(): for embedding raw HTML (tables, styling, formatting).
# Markdown(): to render Markdown strings dynamically.

# -----------------------------------------------------------------------------------------
# Allows us to display output from multiple lines in a single cell
#  (useful when returning multiple objects).
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# --------------------------------------------------------------------------------------
# Automatically reloads modules we edit outside the notebook 
# without restarting the kernel 
# (useful in modular analysis or app development).
%load_ext autoreload
%autoreload 2

# ---------------------------------------------------------------------------------------

#  Adds clean and interactive progress bars in 
# loops and DataFrame operations.
from tqdm.notebook import tqdm

# ------------------------------------------------------------------------------------------

# jupyterthemes: for consistent UI style
# (optional but adds polish when presenting).
!pip install jupyterthemes
# Example (after installing): 
# !jt -t grade3 -ofs 12 -nfs 12 -tfs 12 -cellw 88%

```

## **Important Links:**
1. Python: [Python](https://www.python.org/)

2. Jupyter Notebook: [Jupyter Notebook](https://jupyter.org/)

3. Numpy: [Numpy](https://numpy.org/)

4. Pandas: [Pandas](https://pandas.pydata.org/)

5. Matplotlib: [Matplotlib](https://matplotlib.org/)

6. Seaborn: [Seaborn](https://seaborn.pydata.org/)

7. Plotly: [Plotly](https://plotly.com/python/)

8. Scikit-Learn: [Scikit-Learn](https://scikit-learn.org/stable/)

9. GitHub: [GitHub](https://github.com/)


## **Data Sources:**
Here’s a list of **some popular open data sources** I may use in my projects for data analysis and visuallization:

### **1. Top General Data Repositories (Structured, Tabular Data):**

| Source | Description | Format |
|--------|-------------|--------|
| [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) | The gold standard for classical ML datasets (Iris, Wine, Adult Income, etc.) | CSV, ARFF |
| [Kaggle Datasets](https://www.kaggle.com/datasets) | Rich collection of tabular datasets for ML and visualization. | CSV, Excel |
| [Awesome Public Datasets on GitHub](https://github.com/awesomedata/awesome-public-datasets) | A massive list of categorized datasets (many tabular). | Mixed |
| [OpenML](https://www.openml.org/) | Community-driven ML datasets and tasks. Integrates well with `scikit-learn`. | CSV |
| [DataHub.io](https://datahub.io/) | Open datasets in finance, health, education, etc. (easy to browse by topic). | CSV, JSON |

### **2. Classic & Beginner-Friendly Datasets for ML and Visualization:**

| Dataset | Description | Source |
|---------|-------------|--------|
| **Iris** | Flower classification (ideal for basic classification and clustering). | UCI, scikit-learn |
| **Wine Quality** | Predict quality of red/white wine based on physicochemical tests. | UCI |
| **Titanic Survival** | Predict who survived the Titanic disaster. | Kaggle |
| **Adult Income** | Classification task: predict whether income >$50K/year. | UCI |
| **Boston Housing** | Predict house prices based on 13 features. *(Note: deprecated due to ethical concerns, but still educational)* | scikit-learn |
| **California Housing** | A modern alternative to Boston housing. | scikit-learn |
| **Heart Disease** | Predict presence of heart disease. | UCI |
| **Pima Indians Diabetes** | Classification of diabetes based on diagnostic measures. | UCI |
| **Bank Marketing** | Predict whether a client will subscribe to a term deposit. | UCI |

### **3. Datasets for Data Visualization:**

| Dataset | Description | Source |
|---------|-------------|--------|
| **Gapminder Data** | Global development indicators (life expectancy, income, etc.). | [Gapminder](https://www.gapminder.org/data/) |
| **World Bank Open Data** | Country-level indicators (GDP, inflation, education, etc.). | [World Bank](https://data.worldbank.org/) |
| **COVID-19 Dataset** | Time-series data on global COVID-19 stats. | [Our World in Data](https://ourworldindata.org/coronavirus-source-data) |
| **Airbnb Listings** | Real-world city-level Airbnb listings. | [Inside Airbnb](http://insideairbnb.com/get-the-data.html) |
| **Spotify Charts** | Song popularity and trends. | [Kaggle Spotify datasets](https://www.kaggle.com/datasets) |

### **4. Tools & Libraries that Include Built-In Datasets:**

| Tool | Datasets |
|------|----------|
| `sklearn.datasets` | Built-in datasets like Iris, Diabetes, California Housing. |
| `seaborn.load_dataset()` | Datasets like Titanic, Tips, Flights, Penguins, etc., great for visualization. |
| `plotly.express.data` | Built-in datasets like Gapminder, Iris, Tips for interactive plotting. |


---
---
## **Contributing:**
Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## 📫 **Contact:**
- 📧 Email: russdataproject@gmail.com
- 💼 LinkedIn: [Click Here](https://www.linkedin.com/in/rajesh-kumar-dhimal-478901279/)