def lib(n):
    i = 0
    x = 0
    while (i <= n):
        x = x * 1
        i+=1

    i=1
    while (i <= n):
        x = x + i
        i+=1

    i=1
    while (i <= n):
        x = x * 2
        i+=1


    return x

def barth2(x):
    if (x <10):
        return lib(x)
    else:
        return 0


