"""
1. Create 3 first names
2. Create 3 last names
3. Combine them randomly into a list of 5 full names
"""

import random

first_names = ["John", "Jane", "Jack"]
last_names = ["Smith", "Doe", "Jones"]

full_names = []

for i in range(5):
    full_names.append(random.choice(first_names) + " " + random.choice(last_names))

print(full_names)