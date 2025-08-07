from calculation import calculation
from covariance import covariane_matrix
from correlation import correlation
from portfolio_risk_var import portfolio_risk_var

def  menu(portfolio,stock_owned):
    cov_matrix=None
    while True:
        a=int(input("""What do you want to check of the stock:-
                        1.Overall return percentage
                        2.Covariance Matrix
                        3.Correlation Matrix
                        4.Portfolio Risk 
                        5.Exit:-"""))
        if a==1:
            print(calculation(portfolio,stock_owned))
        elif a==2:
            cov_matrix=covariane_matrix(portfolio,stock_owned)
            print("Covatiance Matrix")
            print(covariane_matrix(portfolio,stock_owned))
        elif a==3:
            print(correlation(portfolio,stock_owned))
        elif a==4:
            if cov_matrix is None:
                print("Compute covariance matrix first.")
            else:
                
                print(portfolio_risk_var(portfolio,stock_owned,cov_matrix))
                
        elif a==5:
            exit_message=print("Exited successfully!!!!")
            return exit_message
        else:
            message="Invalid Input"
            return message
        
