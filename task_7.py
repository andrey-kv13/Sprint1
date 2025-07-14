import random as r

def digit_root(num):
    while num >= 10:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10  
            num = num // 10 
        num = sum_digits
    return num
  
num = r.randint(100, 10**7)
print(digit_root(num))
