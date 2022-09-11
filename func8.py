def func8(n):
    i = 1
    while True:
        res = n * i
        rl = list(str(res))
        if ('1' in rl or
            '2' in rl or
            '3' in rl or
            '4' in rl or
            '5' in rl or
            '6' in rl or
            '8' in rl or
            '9' in rl):
               i = i + 1
        else:
            break
    return res

a = int(input("Input a integer:"))
ans = func8(a)

print(ans)
print(str(a)+"*"+str(int(ans/a))+"=="+str(ans)) 
