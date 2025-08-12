import numpy as np
def initilization():
    np.random.seed(42)
    learning_rate=0.5
    epoch=400100
    input_neuron=2
    hidden_neuron=4
    output_neuron=1
    w1=np.random.randn(input_neuron,hidden_neuron)*0.5
    w2=np.random.randn(hidden_neuron,output_neuron)
    b1=np.ones((1,hidden_neuron))*0.1
    b2=np.zeros((1,output_neuron))

    return w1,w2,b1,b2,epoch,learning_rate

