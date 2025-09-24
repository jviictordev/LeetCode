# Solução convertendo para string
def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1]

print(is_palindrome(121))  # saída: True
print(is_palindrome(-121))  # saída: False
print(is_palindrome(10))  # saída: False
