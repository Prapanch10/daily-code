import random
from datetime import datetime

problems = [
    "Find duplicate in array",
    "Check palindrome string",
    "Find max element in list",
    "Reverse a string",
    "Count vowels in string"
]

problem = random.choice(problems)

filename = datetime.now().strftime("%Y-%m-%d") + ".py"

with open(filename, "w") as f:
    f.write(f"# Problem: {problem}\n\n")
    f.write("# Write your solution here\n")

print("Created:", filename)
