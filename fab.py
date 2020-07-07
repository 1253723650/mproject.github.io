x=int(input("Enter the range"));
a=0;
b=1;
c=0
count=1;
if x == 1:
    print("fab",c,end=" ")
else:
    print("fab",end=" ")
    while count <= x:
        print(c,end = " ")
        count = count+1;
        a=b;
        b=c;
        c=a+b;
