from itertools import count

def is_palindrome(num):
        string = str(num)
        if string == string[::-1]:
                return True

list = []
total = 0

for i in count():
        
        if is_palindrome(i):
                list.append(i)

                if len(list) >= 2000:
                        total = sum(list)
                        break
print(total)
