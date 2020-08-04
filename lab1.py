mas=[3,5,4,-65,34,21]
print(mas)
for i in range(1,len(mas)-1):
    if mas[i+1]<mas[i] and mas[i-1]<mas[i]:
        print(i+1,end=" ")
