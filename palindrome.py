from itertools import count

def is_palindrome(num):
        string = str(num)
        if string == string[::-1]:
                return True

total = 0
counted = 0

for i in count():
        if is_palindrome(i):
            total += i
            counted += 1
        if counted == 2000:
            break

print(total)
