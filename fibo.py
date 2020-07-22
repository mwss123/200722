
l_fibo = [0, 1]

n = int(input('NUM? :'))

for i in range(n-2) :
    new = l_fibo[-2] + l_fibo[-1]
    l_fibo.append(new)

print(f"n_th number is {l_fibo[-1]}")



import sys

def fibo(n : int) -> int :
    if n == 0 :
        return 0

    if n == 1 :
        return 1

    else :
        return fibo(n-1) + fibo(n-2)


n= int(sys.argv[1])

print(fibo(n))
