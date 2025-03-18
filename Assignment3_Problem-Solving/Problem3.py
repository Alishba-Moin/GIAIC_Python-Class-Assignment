# Problem 3: Sum of digits

def sum_of_digits(n):
    
    total = 0

    for digit in str(n):
        total += int(digit)
    return total

sum_num = sum_of_digits(1234)
print(" Sum of Digits:", sum_num)
