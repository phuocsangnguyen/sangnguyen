n = int(input())
if n < 0:
    print("hay nhap so lon hon 0")
else:
    Giaithua = 1
    for i in range (1,n+1):
        Giaithua = Giaithua*i
    print(Giaithua)    