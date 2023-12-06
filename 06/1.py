import math
from sympy import symbols, Interval, solve_univariate_inequality

with open("06/input1") as f:
    lines = f.readlines()
    times = [int(s) for s in lines[0].split(":")[1].split(" ") if s != ""]
    dists = [int(s) for s in lines[1].split(":")[1].split(" ") if s != ""]

prod = 1
for time, record in zip(times,dists):
    p = symbols('p') # pressed time
    inequality = (time*p - p**2 - 1 > record)
    domain = Interval(0, record)
    sol = solve_univariate_inequality(inequality, p, False, domain)
    start = math.ceil(sol.start.evalf())
    end = math.floor(sol.end.evalf())
    ways = abs(end - start) + 1
    prod *= ways
print(prod)
