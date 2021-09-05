def fib(n):
    lis = [0,1]
    i = 2
    if n > 2:
        while i <= n:
            newitem = lis[-1] + lis[-2]
            lis.append(newitem)
            i += 1
    elif n == 1:
        return (lis[-2])
    return (lis[-1])    

i = 1
while i < 10:
    print( 'fib(',i,') : ', fib(i) )
    i+=1
