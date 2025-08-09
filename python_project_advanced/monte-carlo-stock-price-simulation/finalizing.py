import numpy as np
def finalizing(final_day_price,loss_count):
    average=np.average(final_day_price)
    max_p=np.max(final_day_price)
    min=np.min(final_day_price)
    loss_count=loss_count/np.size(final_day_price)
    

    avg=print(f"Your final days average price= ₹ {np.round(average,2)}")
    max_price=print(f"Your maximum price= ₹ {np.round(max_p,2)}")
    min_price=print(f"Your minimum price= ₹ {np.round(min,2)}")
    loss_percent=print(f"Your percentage of simulation that ended in loss={loss_count*100}%")
    


    return avg,max_price,min_price,loss_percent