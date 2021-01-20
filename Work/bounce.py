# bounce.py
#
# Exercise 1.5

# A rubber ball is dropped from a height of 100 meters and each time it hits
# the ground, it bounces back up to 3/5 the height it fell. Write a program
# bounce.py that prints a table showing the height of the first 10 bounces.

height = 100 # meters
bounce_back = 3.0 / 5.0
bounce_heigt = height

for i in range(10):
    bounce_heigt = bounce_heigt * bounce_back
    print(i + 1, round(bounce_heigt, 4))
