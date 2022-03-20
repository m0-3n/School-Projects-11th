l = []
flag = False
n = int(input('Enter number of elements: '))
for i in range(n):
    e = int(input(f'Enter element: '))
    l.append(e)
print(l)
s = int(input('Enter element to search: '))
for i in l:
    if l[i] == s:
        print(s,'was found in the list as position:', l.index(s))
        flag = True
        break

if flag == False:
    print(s, 'was not found in the list.')
        
        

