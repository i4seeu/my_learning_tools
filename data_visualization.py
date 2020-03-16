import  pandas as pd
import  numpy as np
from matplotlib import pyplot as plt
import  seaborn as sns

df = pd.read_csv('Pokemon.csv',index_col=0,encoding='ISO-8859-1')

sns.lmplot(x='Attack',y='Defense', data=df)
plt.show()