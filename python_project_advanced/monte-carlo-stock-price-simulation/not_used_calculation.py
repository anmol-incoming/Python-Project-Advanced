#This is the first logic i used in monte carlo stock simulation using gbm.
#But later found out sim X days is better and used widely.
""""
import numpy as np
def calculation(initial_price,expected_return,volatility,no_days,simulation):
    calculation_list=[]
    current_price=np.full(simulation,initial_price)
    volatility=np.full(simulation,volatility)
    expected_return=np.full(simulation,expected_return)
    epsilon=np.random.normal(0,1,size=(no_days,simulation))
    print(epsilon)
    dt=1/252
    k=5
    m=0.5
    for i in range(no_days):
        for j in range(simulation):
            new_price=current_price[j] * np.exp((expected_return[j]-0.5*volatility[j]**2)*dt + volatility[j] *epsilon[i,j]*np.sqrt(dt))
            calculation_list.append(new_price)
            volatility[j]=volatility[j] *(1 +k *(current_price[j]-new_price)/current_price[j])
            expected_return[j]=expected_return[j]-m*(new_price-current_price[j])/current_price[j]
            current_price[j]=new_price
     
    
    calculation_list=np.array(calculation_list)

    return calculation_list
"""
            