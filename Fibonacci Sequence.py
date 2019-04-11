nterm = int(input("Enter number of sequence"))
n1 = 0
n2 = 1
count = 0

if nterm<=0:
    print("Please enter positive number")
elif nterm==1:
    print("fibonacci sequence ",nterm, "is: ", n1)
else:
    print("fibonacci sequence of",nterm,": ")
    while count<nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1
        
        
  output:
  Enter number of sequence10
fibonacci sequence of 10 : 
0
1
1
2
3
5
8
13
21
34
