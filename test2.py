import json
import numpy as np

def f(x):
    return np.sin(x)

x = np.linspace(-10, 10, 400).tolist()
y = f(np.array(x)).tolist()

data = {'x': x, 'y': y}

with open('plot_data.json', 'w') as f:
    json.dump(data, f)