#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import japanize_matplotlib

import sys
import os

from yokotools import mysets
#from mytools import mycolors

# %%
colors = mysets.Color()
pastel = colors.pastel()

# %%
x = ["LLaMA-13B", "Alpaca-13B", "Vicuna-13B", "Bard", "ChatGPT"]
y = [68, 76, 92, 93, 100]

plt.bar(x, y, color=[
        pastel["gray"],
        pastel["gray"],
        pastel["yellow"],
        pastel["blue"],
        pastel["green"]
    ]
)
plt.show()

# %%
