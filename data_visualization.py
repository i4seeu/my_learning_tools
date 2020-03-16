import  pandas as pd
import  numpy as np
from matplotlib import pyplot as plt
import  seaborn as sns

df = pd.read_csv('Pokemon.csv',index_col=0,encoding='ISO-8859-1')

sns.lmplot(x='Attack',y='Defense', data=df, fit_reg=False, hue='Stage')

#customizing the axes with matplotlib
plt.ylim(0,None)
plt.xlim(0,None)

# Pre-format DataFrame
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
# New boxplot using stats_df
#sns.boxplot(data=stats_df)

#setting theme
sns.set_style('whitegrid')

#visualise the distribution of attach by pokemons type using violinplot
#sns.violinplot(x='Type 1', y='Attack', data=df)
# Swarm plot with Pokemon color palette
#sns.swarmplot(x='Type 1', y='Attack', data=df)

# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.Attack)
plt.show()