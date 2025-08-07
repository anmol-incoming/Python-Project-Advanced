import numpy as np
def correlation(portfolio,stock_owned):
    returns=[]
    for i in portfolio:
        for j in i["return"]:
            returns.append(j)
    final_return=np.array(returns).reshape(stock_owned,5)
    corr_mat=np.corrcoef(final_return)


    return corr_mat