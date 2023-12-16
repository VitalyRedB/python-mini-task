'''
Code Challenge: The Z-Score (or Standard Score) is a numerical statistic assigned to a number N to indicate how far N is from the mean of a given set of numerical data numbers. The Z-Score of N when compared to numbers is computed using the formula:

N−mean(numbers)   /   stdev(numbers)
​
Write a function find_z_score() that takes in a float value N and a list of float values numbers and returns the Z-Score of N with respect to numbers.

Note: You can import packages inside of a function, too!

Example: If N = 5 and numbers = [0, 4, 8], then find_z_score(N, numbers) should return 0.25. 
'''
import statistics
def find_z_score(N, numbers):
    
    z_score = (N - statistics.mean(numbers)) / statistics.stdev(numbers) if len(numbers) > 1 else None
    return z_score
  
