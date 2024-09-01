import random
code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]
code_3_digit_str = ''.join(map(str, code_3_digit))
code_4_digit_str = ''.join(map(str, code_4_digit))
print(f"The 3-digit combination lock code is: {code_3_digit_str}")
print(f"The 4-digit combination lock code is: {code_4_digit_str}")
