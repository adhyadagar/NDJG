import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv('test.csv', index_col=False)

print(type(data))

#data.loc["Delhi"] = data.loc["Delhi"]/593907
#data.loc["Maharashtra"] = data.loc["Maharashtra"]/248326
#data.loc["Tamil Nadu"] = data.loc["Tamil Nadu"]/502030
#data.loc["Uttar Pradesh"] = data.loc["Uttar Pradesh"]/5744621
#data.loc["West Bengal"] = data.loc["West Bengal"]/1770629

corr = data.corr()

print(corr)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()

'''
#fig = plt.figure()
#ax = fig.add_subplot(111)
#cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
ax = sns.heatmap(corr ,vmin=-1, vmax=1, annot=True)
#fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()
'''
