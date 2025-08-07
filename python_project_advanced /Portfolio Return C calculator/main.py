from user_inp import user_inp
from menu import menu
def main():
    portfolio,stock_owned=user_inp()
    
    
    result=menu(portfolio,stock_owned)

    return result
run=main()
 #[2, 3, 1, 4, 5],[1, 0, -1, 2, 1]-- these are sample test return value
