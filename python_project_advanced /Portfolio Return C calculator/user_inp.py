def user_inp():

    portfolio=[]
    
    stock_owned=int(input("How many stock you own:-"))
    for i in range(stock_owned):
        returns=[]
        stock_name=input("Enter the name of the stock:-")
        stock_investement=int(input(f"Enter the amount you invested in {stock_name} :-"))
        print("Enter 5 months of returns value for the stock....")
        for i in range(5):           
            stock_return=float(input(f"Enter the stock return of {stock_name} for month {i+1}:-"))
            returns.append(stock_return)
        print(f"{stock_name} added successfully.........")
        info={"name":stock_name,"return":returns,"investement":stock_investement}
        portfolio.append(info)
    #print(portfolio)
    print("Portfolio values stored succesfully")
    return portfolio,stock_owned

