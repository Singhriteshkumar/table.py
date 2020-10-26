#   write a program a table use to python
#   program written by Ritesh Kumar Singh
S=int(input("enter a starr table :"))
l=int(input("enter a last table :"))
i=1
while(i<=10):
    s=S
    while(s<=l):
        T=s*i
        if T>=100:
            print(T, end=" ")
        elif T>=10:
            print(T, end="  ")
        else:
            print(T, end="   ")
        s+=1
    i+=1
    print()