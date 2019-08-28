for n in range (2,100):
    for x in range (2,n):
        if n % x == 0:
            print(n,"es ingual a ", x,"*",n/x)
    else:
        print(n, "es un numero primo")
