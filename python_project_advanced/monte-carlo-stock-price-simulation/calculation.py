import numpy as np
def calculation(initial_price,expected_return,volatility,no_days,simulation):
    calculation_list=[]
    final_day_price=[]
    current_price=initial_price
    epsilon=np.random.normal(0,1,size=(simulation,no_days))
    dt=1/252
    k=5
    m=0.5
    initial_expected_return=expected_return
    initial_volatility=volatility
    for i in range(simulation):
        current_price=initial_price
        volatility=initial_volatility
        expected_return=initial_expected_return
        for j in range(no_days):
            new_price=current_price * np.exp((expected_return-0.5*volatility**2)*dt + volatility *epsilon[i,j]*np.sqrt(dt))
            calculation_list.append(new_price)
            new_volatility=volatility *(1 +k *(current_price-new_price)/current_price)
            new_expected_return=expected_return-m*(new_price-current_price)/current_price
            current_price=new_price
            volatility=new_volatility
            expected_return=new_expected_return
        final_day_price.append(calculation_list[-1])
            
    calculation_list=np.array(calculation_list)
    final_day_price=np.array(final_day_price)
    loss_count=np.sum(final_day_price<initial_price)
    
   

    return final_day_price,loss_count

            