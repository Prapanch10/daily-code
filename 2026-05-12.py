# Problem: Find duplicate in array
oh my god
# Write your solution here
def duplicate(arr):
  seen = set()
  for i in arr:
    if i in seen:
      return "duplicate found"
    seen.add(i)
  return "not found"

arr = [1,2,3,4,5,3,5,5]

print(duplicate(arr))
    
