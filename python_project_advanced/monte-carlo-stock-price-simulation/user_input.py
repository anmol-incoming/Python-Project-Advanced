def user_input():
    initial_price=float(input("Enter the initial price of the stock in ₹:-"))
    expected_return=float(input("Enter the expected return in %:-"))
    volatility=float(input("Enter the volatility of the stock in %:-"))
    no_days=int(input("Enter number of days you want to run simulation for:-"))
    simulation=int(input(f"Enter the number of simulation you want to run for {no_days} days:-"))
    volatility=volatility/100
    expected_return=expected_return/100

    return initial_price,expected_return,volatility,no_days,simulation