"""Generate the 180-day synthetic bike demand set. Seed is fixed so every
student's data is identical and results are reproducible.

    python -I generate_data.py > bike_demand.csv
"""
import math
import random

random.seed(42)
print('day,weekday,temp,rain,demand')
for day in range(1, 181):
    weekday = day % 7
    temp = 15 + 10 * math.sin(day / 28) + random.uniform(-2, 2)
    rain = 1 if random.random() < 0.25 else 0
    demand = max(0, round(40 + 2 * temp - 18 * rain + 10 * (weekday < 5)
                          + random.uniform(-8, 8)))
    print(f'{day},{weekday},{temp:.3f},{rain},{demand}')
