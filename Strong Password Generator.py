import random

print("STRONG PASSWORD GENERATOR")
print()

class WrongLength(Exception):
    pass
try:
    print("Enter Password Length : ",end="")
    length=int(input())
    
    if(length<=8):
        raise WrongLength("For a Password to be *Strong*,its length should be greater than 8.Enter again!!")
    
    characters=r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=:<>?/}|{;'.,`~-[\]$\""
    pwd=[]
    print("Password : ",end="")

    for i in range(length):
        ch=random.choice(characters)
        pwd.append(ch)
        print(ch,end="")
    
except ValueError:
    print("Please enter a valid number!!")
except WrongLength as w:
    print(w)

