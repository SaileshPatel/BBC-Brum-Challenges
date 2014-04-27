from itertools import count

def is_palindrome(num):
        numString = str(num)
        if numString == numString[::-1]:
                return True
        
total = 0
palindromeList = []
counted = 0

for i in count():
        if counted >= 2000:
                break

        if is_palindrome(i):
                print(i)
