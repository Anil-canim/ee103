n="nooooooo"
b=int(len(n))
while b>2:
    print(n)
    n= n[-1::1]
print("no")

mysum=0
start=3
end=5
for i in range(start,end+1):
    print("i=",i)
    mysum += i
    
