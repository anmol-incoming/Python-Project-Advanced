This project is based on XOR neural network.
No deep learning libraries like pytorch,keras etc is used just created the whole neural network using numpy concept.

First thing i did is to create a traing set where i defined input and output.Then initialized weights ,biases, no.of hidden layer , input layer ,output layer , learning rate and epoch used np.random.seed(42) to get fixed numbers.Later on defined activation functions first i started with sigmoid but after not getting desired reslult after fine tuning weights , biases moved to relu and later on combined both to get better result.Then trained the model for 400,000 epoch with learning rate =0.5 got this 
output:- 
Epoch 400000 Loss: 6.666207804758776e-07
Final Prediction:-
[[0.001]
 [0.999]
 [0.999]
 [0.001]]

 Thank you for reading this.Hope You have a great day.

 # note i tried just now with sigmoid only as well just enure that you ajust the intial weights * 0.5 and one of the biases to np.ones to get good results and when better reult by using relu as activation  and leaky relu as derivative.enure weights and biases are blanced output using relu and leaky relu -
Final predictions:
[[0.001]
 [0.999]
 [1.   ]
 [0.001]] # this is with 8500 epoch only  converged faster.



