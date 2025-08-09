from user_input import user_input
from calculation import calculation
from finalizing import finalizing
def main():
    initial_price,expected_return,volatility,no_days,simulation=user_input()
    final_day_price,loss_count=calculation(initial_price,expected_return,volatility,no_days,simulation)
    result=finalizing(final_day_price,loss_count)
    return result
run=main()
