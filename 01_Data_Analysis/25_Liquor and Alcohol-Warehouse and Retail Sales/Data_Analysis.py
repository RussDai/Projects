<<<<<<< HEAD
#  Disable future warnings:
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# %matplotlib inline

from Data_Cleaning_and_Preparation import load_and_prepare_data

data = load_and_prepare_data()

# Overall Top selling items:
daa= data.groupby(by= "item description")["retail sales"].sum().sort_values(ascending= False).head(10)
daa= daa.reset_index()

# Using Seaborn: 
plt.figure(figsize= (6,6))
sns.barplot(data= daa, x= "retail sales", y= "item description")
=======
#  Disable future warnings:
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# %matplotlib inline

from Data_Cleaning_and_Preparation import load_and_prepare_data

data = load_and_prepare_data()

# Overall Top selling items:
daa= data.groupby(by= "item description")["retail sales"].sum().sort_values(ascending= False).head(10)
daa= daa.reset_index()

# Using Seaborn: 
plt.figure(figsize= (6,6))
sns.barplot(data= daa, x= "retail sales", y= "item description")
>>>>>>> 389f30ffef1a17d195c89a879bd2adc4c3404cdc
plt.show()