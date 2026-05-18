# Problem: Reverse a string

# Write your solution here
def reverse(name):
  new_name = ""
  for i in range(len(name)-1,-1,-1):
    new_name += name[i]
