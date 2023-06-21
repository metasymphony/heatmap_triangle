## HEATMAP ##
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#for jupyter notebook
%matplotlib inline
%config InlineBackend.figure_format = 'retina'

# change df to your DataFrame name. if needed, drop columns here.
mean_corr = df.corr()
# Set the default matplotlib figure size to 20x14 or resize as needed.
fix, ax = plt.subplots(figsize=(20,14))
# Generate a mask for the upper triangle - taken from seaborn example gallery.
mask = np.zeros_like(mean_corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Assign the matplotlib axis the function returns. This will let you resize the labels.
ax = sns.heatmap(mean_corr, mask=mask, ax=ax, annot=True, cmap='RdBu', vmin=-1, vmax=1)
# Resize and rotate the labels
ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14, rotation=90)
ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14, rotation=0)
# Prevents printouts from matplotlib.
plt.show()
