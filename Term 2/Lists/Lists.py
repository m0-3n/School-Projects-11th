l=eval(input("Enter a list of numbers: "))
z=0
p=0
n=0
for i in range(len(l)):
    if l[i]==0:
        z+=1
    elif l[i]>0:
        p+=1
    else:
        n+=1
print(l)
print("Total No. of zeros in the list are:",z)
print("Total No. of positive numbers in the list are:",p)
print("Total No. of negative numbers in the list are:",n)
