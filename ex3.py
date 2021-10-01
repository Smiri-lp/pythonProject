import math

num = int(input("Let us know your number: "))

def power(num):
    if (num>0 and math.log2(num).is_integer()):
        print(f"{num} yayy!!!!! You got the  power of 2")
    else:
        print(f"{num}? Maybe you'll be lucky next time ")
power(num)