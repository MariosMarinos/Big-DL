import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data2.txt", ",")

fig,ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_title('Learning rate optimization')
cost_line, = ax.plot(data.lr, data.cost, color="red", marker="o")
ax.set_xlabel("Learning rate",  fontsize=14)
ax.set_ylabel("Cost",color="red",  fontsize=14)

ax2=ax.twinx()
acc_line, = ax2.plot(data.lr, data.acc ,color="blue",marker="o")
ax2.set_ylabel("Accuracy", color="blue", fontsize=14)

plt.show()
fig.savefig('optimization.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

plt.show()