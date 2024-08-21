""" Write a Python program to convert degree to radian"""
import math

degree = float(input("Enter degree: "))

radian = degree * (math.pi / 180)

print(f"{degree} degrees is equal to {radian} radians")
