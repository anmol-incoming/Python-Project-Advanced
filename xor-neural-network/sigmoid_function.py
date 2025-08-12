import numpy as np
def sigmoid_function(x):
    sig=1/(1+np.exp(-x))
    return sig