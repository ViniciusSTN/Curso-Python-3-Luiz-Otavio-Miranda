num_1 = 0.7
num_2 = 0.1
num_3 = num_1 + num_2

print(num_3)
print(f'{num_3:.2f}')
print(round(num_3, 2))

# ou então
import decimal

num_4 = decimal.Decimal('0.7')
num_5 = decimal.Decimal('0.1')
num_6 = num_4 + num_5
print(num_6)