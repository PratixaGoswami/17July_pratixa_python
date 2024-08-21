""" Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.

"""
import itertools
Sample_data={'1': ['a','b'], '2': ['c','d']}
value=dict.values(Sample_data)
combination=list(itertools.product(*value))
print(combination)

