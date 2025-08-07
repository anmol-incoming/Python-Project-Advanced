import numpy as np
def covariane_matrix(portfolio,stock_owned):
    returns=[]
    for i in portfolio:
        for j in i["return"]:
            returns.append(j)
    final_return=np.array(returns).reshape(stock_owned,5)
    mat_return=final_return.T  
# it does not matter the shape of the matrix in the end it will give 2,2 matrix.But if you conv 2,5 to 5,2 make sure you use rowvar=False as it is true by default. while answer will be same even if its 5,2 or 2,5 ..
    
    cov_matrix=np.cov(mat_return,rowvar=False)
    return cov_matrix
