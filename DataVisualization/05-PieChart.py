import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv('SaratogaHouses.csv')
print(dataset.head())

x = dataset['fuel']
x = pd.value_counts(x)
print(x)
y = np.array([x[0],x[1],x[2]])
plt.pie(y, labels=['gas','electric','oil'], autopct='%0.0f%%', shadow=True,
        startangle=90, explode=[0.2,0,0])
plt.legend()
plt.show()
