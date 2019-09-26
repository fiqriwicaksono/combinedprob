from scipy.stats import binom
from matplotlib import pyplot as plt
import numpy as np
import collections as col

# Taking inputs
p = input('What is the probability of event x?')
n = input('How many trial do you want to conduct?')
x = input('How many event x do you wish the probability to be calculated? \n*Please use comma (,) if  u want to calculate more than 1 probabilities*')

#def counter(list):
#    ctr = 0
#    for li in range(len([list]+1)):
#        ctr += 1
#    return ctr

if p > 1:
    print('The probability of an event cannot be more than 100%')
elif p == 1:
    print('The probability  is certain')
else:
    if len(str(x)) > 1:
        prob = binom.pmf(x, n, p)
        # Set up the graph
        plt.xlabel('k')
        plt.ylabel('Probability')
        plt.bar(x, prob)
        plt.show()
    else:
        prob = binom.pmf(x, n, p)
        # Set up the graph
        plt.xlabel('k')
        plt.ylabel('Probability')
        plt.scatter(x, prob)
        plt.show()

