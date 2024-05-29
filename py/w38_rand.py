#!/usr/bin/python
print('Content-type: text/html\n')

import random

# Printing some text
print("<html><body>")
print("<h1>Welcome to our random number generator page!</h1>")

# Generating and printing a random number
random_number = random.randint(1, 100)
print(f"<p>Your random number is: {random_number}</p>")

print("</body></html>")
