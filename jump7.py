a=0
while a<100:
    a=a+1
    if a%7==0:
        continue
    if a%10==7:
        continue
    if a in range(70,80):
        continue
    print(a)
