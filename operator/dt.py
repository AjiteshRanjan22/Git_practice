'''Calculate total bill, with user inputs and repeating as per user wish'''

import sys

def solve(meal_cost, tip_percent, tax_percent):
    if meal_cost < 0 or tip_percent < 0 or tax_percent < 0:
        print('Invalid entry: try again')
        return False

    totalMealCost = int(round(meal_cost + ((tip_percent/100)*meal_cost) + ((tax_percent/100)*meal_cost)))
    print(totalMealCost)



print('what is the cost of meal?')
meal = int(sys.stdin.readline())

print('what is the tip?')
tip = int(sys.stdin.readline())

print('what is the tax?')
tax = int(sys.stdin.readline())

solve(meal, tip, tax)