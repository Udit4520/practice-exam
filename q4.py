n = int(input("Enter a number : "))
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*int(i)+1))