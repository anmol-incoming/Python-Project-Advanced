import numpy as np
def activation_function(x):
    relu=np.maximum(0,x)
    return relu