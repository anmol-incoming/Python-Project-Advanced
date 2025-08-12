import numpy as np
def training_set():
    inputs=np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ])

    outputs=np.array([
        [0],
        [1],
        [1],
        [0]
    ])

    return inputs,outputs