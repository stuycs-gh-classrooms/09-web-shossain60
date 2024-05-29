#!/usr/bin/python
print('Content-type: text/html\n')

import random

random_number = random.randint(1, 100)
print(f"<p>Your random number is: {random_number}</p>")

