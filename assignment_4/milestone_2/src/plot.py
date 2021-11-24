import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

paths = ['data/10_2.csv', \
         'data/50_5.csv', \
         'data/100_10.csv']

plt.xlabel('completion time (seconds)')
plt.ylabel('norm dist')

plt.title(f'MapReduce Completion Times Comparison')

for path in paths:
    data = pd.read_csv(path)

    x = data['completion time']
    y = data['norm dist']

    plt.plot(x, y, marker='o',label=path.replace('.csv', ''))

    quant_90 = np.percentile(data['completion time'], 90)
    quant_95 = np.percentile(data['completion time'], 95)
    quant_99 = np.percentile(data['completion time'], 99)

    quants = [[quant_90, 0.6, 'r'], [quant_95, 0.8, 'g'], [quant_99, 1, 'b']]
    for q in quants:
        plt.axvline(q[0], alpha = q[1], color = q[2], linestyle = ":")

plt.legend(loc=(1.02,0))
plt.show()