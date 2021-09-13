import tensorflow
import numpy as np
import pandas


def act (x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    weight1 = np.array([[0.3, 0.3, 0], [0.4, -0.5, 1]])
    weight2 = np.array([-1, 1])

    sum_hidden = np.dot(weight1, x)
    print(sum_hidden)

    out_hidden = np.array([act(x) for x in sum_hidden])
    print(out_hidden)
    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print(y)

#go(1,0,1)