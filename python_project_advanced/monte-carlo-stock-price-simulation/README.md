This is a baisc level Monte-carlo-simulation using Geometric Brownian Motion (GBM).

In this project We input intial price,return and volatility then it gets updated dynamically using gbm , volatility and return formula for each day and the value of final day of each simulation gets stroed in the list. which is converted to array for easy calculation and avoiding loops for calculating 1.average/mean ,2.max price ,3.min_price and 4. percentage of simulation that ended in loss of last day of each simulation only .

used np.random.normal(0,1) to introduce randomness and the size was simulation x days.

Note- the not_used_calculation.py file is correct and working.Basically not used because of differnet logic it was looped in  day x simulation where as mote carlo is basically simulation x day .

used -numpy concepts, forloops, function etc.

Thank you for reading this.Hope you have a great day.
