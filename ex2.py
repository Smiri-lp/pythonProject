num = int(input("Choose your number: "))
store_num = num
rev_num = 0

while(num>0):
    dig = num%10
    rev_num=rev_num*10+dig
    num = num // 10

if(store_num==rev_num):
    print(f"This is what you are looking for {rev_num}")
else:
    print("Noot palindrome so sad :(")