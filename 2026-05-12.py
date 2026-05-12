# Problem: Count vowels in string

# Write your solution here
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count


text = "hello world"
print(count_vowels(text))
