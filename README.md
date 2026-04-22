# Data Profiling app using Ydata-Profiling

## 1. Installation

to run this app you need to have python installed on your PC. You can install install the required packages using pip:

``` bash
conda create -n ydata-profiling python=3.12 -y
pip install ydata-profiling
conda activate ydata-profiling
pip install streamlit
```

## 2. Execution

create a "app.py" file and run this prompt using github copilot to generate code:
create an app using streamlit where a user drag and drop the data and app automatically create and show rhe y data profiling report in the same page. Please also add some datasets if the user just wanted to see the report. here is how I was doing in the jupitor notebook. import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport
df = sns.load_dataset("diamonds")
profile = ProfileReport(df, title="Profiling Report of Diamonds Dataset")
profile.to_file("diamonds_ydata_profiling_report.html")
profile.to_notebook_iframe()

after this run this code in the bash to run streamlit app:

``` bash

streamlit run app.py
```
