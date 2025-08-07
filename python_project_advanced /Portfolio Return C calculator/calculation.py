import numpy as np
def calculation(portfolio,stock_owned):
    weight_li=[]
    return_li=[]
    total_investement=np.sum([i["investement"]for i in portfolio])
    for i in portfolio:
        weight=i["investement"]/total_investement*100
        r=weight/100
        weight_li.append(r)
    final_weight=np.array(weight_li).reshape(stock_owned,1)
    for i in portfolio:
        for j in i["return"]:
            returns=j/100
            return_li.append(returns)       
    final_return=np.array(return_li).reshape(stock_owned,5)
    transpose_return=final_return.T
    mean=np.mean(transpose_return,axis=0)
    final_total_return_percentage=np.dot(mean,final_weight)
    final_result=np.sum(final_total_return_percentage)*100
    calc_message=f"Your final weighted return of the stock is {np.round(final_result,3)} %"
    return calc_message
        


