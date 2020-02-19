#!/usr/bin/python

import argparse

def find_max_profit(prices):
  bestEntry = 0
  bestExit = 0

  for i in range(len(prices)): 
    if prices[i] < bestEntry or bestEntry == 0:
      for j in range(i+1, len(prices)):
          if prices[j] >= bestExit or bestExit < prices[i]:
            if (prices[j] - prices[i] > bestExit - bestEntry) or (bestExit==0 and bestEntry==0):
              bestExit = prices[j];
              bestEntry = prices[i];

  return bestExit-bestEntry


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))