import random
def green(s,s1,li):
    g=0
    for i in range(len(s)):
            if s[i]==li[i]:
                g=g+1
    return g
def yellow(s,s1,li):
    y=0
    for ch in li:
        for i in range(len(s)):
            if ch==s[i]:
                y=y+1
    g=0
    for i in range(len(s)):
            if s[i]==li[i]:
                g=g+1
    y1=y-g
    return y1
print("\n")
print("\t\t--- HARDWORD CO ---")
li1=["heat","live","peak","time","fame","hole","joke","your","ceal","word","goat","flat","flow","help","pole","fail","take","cake","bake","give","heal"]
s1=random.choice(li1)
for i in range(1,9):
    print("\nATTEMPT No.",i)
    s=input("Enter four-letter word: ")
    try:
        li=list(s1)
        g2=green(s,s1,li)
        y2=yellow(s,s1,li)
        if g2==4:
            print("\tgreen: ",g2)
            print("\tyellow:",y2)
            print("\t\tCONGRATULATIONS...YOU WIN!!!")
            break
        else:
            print("\tgreen :",g2)
            print("\tyellow:",y2)
        if i==8 and g2!=4:
            print("\t\tYou've reached maximum attempts!\n\t\tThe word is:",s1)
    except IndexError:
        print("Not a 4-letter word")
print("\t\tHope you enjoyed!THANK YOU..!")


#beww
import random
def green(s,s1,li):
    g=0
    for i in range(len(s)):
            if s[i]==li[i]:
                g=g+1
    print(" "*8+"green:",g)
    if g==4:
        print("CONGRATSS...YOU WIN!!!!")
def yellow(s,s1,li):
    y=0
    for ch in li:
        for i in range(len(s)):
            if ch==s[i]:
                y=y+1
    g=0
    for i in range(len(s)):
            if s[i]==li[i]:
                g=g+1
    print(" "*8+"yellow:",y-g)
"--- HARDWORD CO ---"
li1=["heat","live","peak","time","fame","hole","joke","your","ceal","word","goat","flat","flow","help","pole","fail","take","cake","bake","give","heal"]
s1=random.choice(li1)
for i in range(1,9):
    print("\nATTEMPT NO:",i)
    print("enter four-letter word:")      
    s=input()
    li=[]
    li=list(s1)
    green(s,s1,li)
    yellow(s,s1,li)    
print("hope you enjoyed!THANK YOU..!")


#new
import random
def green(s,s1,li):
    g=0
    for i in range(len(s)):
            if s[i]==li[i]:
                g=g+1
    return g
def yellow(s,s1,li):
    y=0
    for ch in li:
        for i in range(len(s)):
            if ch==s[i]:
                y=y+1
    g=0
    for i in range(len(s)):
            if s[i]==li[i]:
                g=g+1
    y1=y-g
    return y1
print("\n")
print("\t\t--- HARDWORD CO ---")
li1=["heat","live","peak","time","fame","hole","joke","your","ceal","word","goat","flat","flow","help","pole","fail","take","cake","bake","give","heal"]
s1=random.choice(li1)
for i in range(1,9):
    print("\nATTEMPT No.",i)
    s=input("Enter four-letter word: ")
    li=list(s1)
    g2=green(s,s1,li)
    y2=yellow(s,s1,li)
    if g2==4:
        print("\tgreen: ",g2)
        print("\tyellow:",y2)
        print("\t\tCONGRATULATIONS...YOU WIN!!!")
        break
    else:
        print("\tgreen :",g2)
        print("\tyellow:",y2)
    if i==8 and g2!=4:
        print("\t\tYou've reached maximum attempts!\n\t\tThe word is:",s1)
print("\t\tHope you enjoyed!THANK YOU..!")
    


        
    
    