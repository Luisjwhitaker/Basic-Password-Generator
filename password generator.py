import random
import string

password_length = 26

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = ['0','1','2','3','4','5','6','7','8','9']
ssymbols = ['!','@','%','^','&','*']

lower_selected = True
upper_selected = True
numbers_selected = True
ssymbols_selected = True

bucket = []
final = []

if lower_selected:
    for letter in lower:
        bucket.append(letter)

if upper_selected:
    for letter in upper:
        bucket.append(letter)

if numbers_selected:
    for number in numbers:
        bucket.append(number)

if ssymbols_selected:
    for symbol in ssymbols:
        bucket.append(symbol)

for i in range(password_length):
    final.append(random.choice(bucket))

print(''.join(final))
