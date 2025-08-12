import numpy as np
def derivative_activation(x,alpha=0.01):
    derivative_relu=np.where(x>0,1,alpha)
    return derivative_relu