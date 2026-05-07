import random
num=random.randint(1,100)
print("\n\t\t--NUMBER GUESSING GAME--\n")
while(1):
    n=int(input("Enter any number of your choice(1-100):"))
    if n>num:
        print("below",n)
    elif n<num:
        print("above",n)
    else:
        print("\n\t\t\tCONGRATULATIONS!!\n")
        print("\t\tYou guessed it right! It is",n)
        print("\n")
        break