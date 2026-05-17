# Problem: Find duplicate in array

# Write your solution here
def duplicates(mylist):
  seen = set()
  for i in mylist:
    if i not in seen:
      mylist.remove(i)
    seen.add(i)
  return mylist
