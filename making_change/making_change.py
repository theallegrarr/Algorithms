#!/usr/bin/python

import sys

def making_change(amount, denominations):
  changeVariants={0:1}
  for denomination in denominations:
    for higher_amount in range(denomination,amount+1):
        try:
          changeVariants[higher_amount]+=changeVariants[higher_amount-denomination]
        except:
          changeVariants[higher_amount]=1
  return changeVariants[amount] 


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")