import numpy as np 
import pandas as pd 
import scipy.stats as stats
from statsmodels.stats.proportion import proportions_ztest

# Cargar datos
df = pd.read_excel('diabetes.xlsx')

df.head()