import numpy as np

def portfolio_risk_var(portfolio,stock_owned,cov_matrix):
    #investement=[]
    #for i in portfolio:# This can work too but better is list comprhension
        #money=i["investement"]
        #investement.append(money)
    investement=([i ["investement"]for i in portfolio])
    weights=np.array(investement).reshape(stock_owned,1)
    weights=weights/100
    portfolio_risk_variance=np.dot(weights.T,np.dot(cov_matrix,weights))
    final_std=np.sqrt(portfolio_risk_variance)
    final_ans=np.round(final_std,2)
    return f"Portfolio Risk :-{final_ans.item()}%"
    