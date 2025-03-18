# Problem 2: Count the vowels

def count_the_vowels(s: str) -> int:

    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

# Use a loop and check if each character is in a set of vowels.
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

count_char = count_the_vowels("Apple")
print("Count Vowels:", count_char)