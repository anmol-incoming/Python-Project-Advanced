from training_set import training_set
from initilization import initilization
from Relu_function import activation_function
from leaky_relu_derivative_activation import derivative_activation
from model_training import model_training
from sigmoid_function import sigmoid_function
from sigmoid_derivative import sigmoid_derivative
def main():
    inputs,outputs=training_set()
    w1,w2,b1,b2,epoch,learning_rate=initilization()
    relu=activation_function
    derivative_relu=derivative_activation
    sig=sigmoid_function
    sig_dev=sigmoid_derivative
    result=model_training(inputs,outputs,w1,w2,b1,b2,epoch,learning_rate,relu,derivative_relu,sig,sig_dev)
    print(result)
run=main()


    


