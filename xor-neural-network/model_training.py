import numpy as np
def model_training(inputs,outputs,w1,w2,b1,b2,epoch,learning_rate,relu,derivative_relu,sig,sig_dev):
    
    for i in range(epoch):
        z1=np.dot(inputs,w1)+b1
        a1=relu(z1)
        
        z2=np.dot(a1,w2)+b2
        a2=sig(z2)
        

        mse_error=(a2-outputs)/2  #this is the derivative of mse  
        delta2=mse_error*sig_dev(a2)
        delta1=np.dot(delta2,w2.T)*derivative_relu(a1)

        delta_w2=learning_rate*np.dot(a1.T,delta2)
        w2-=delta_w2
        delta_b2=learning_rate*np.sum(delta2,axis=0,keepdims=True)
        b2-=delta_b2
        delta_w1=learning_rate*np.dot(inputs.T,delta1)
        w1-=delta_w1

        delta_b1=learning_rate*np.sum(delta1,axis=0,keepdims=True)
        b1-=delta_b1

        if i %1000==0:
            loss = np.mean((outputs - a2) ** 2)
            print(f"Epoch {i} Loss: {loss}")


    print("Final Prediction:-")
    return np.round(a2,3)















        











        



    