# Problem1: Reverse a string

def reverse_str(s: str) -> str:
    # Use Python's slicing feature.
    return s[:: -1]


my_str = reverse_str("hello")
print("Reverse a String:", my_str)
