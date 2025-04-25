def run_func(a,b):
    return lambda c:a+b+c
return_func=run_func(1,10000)
print(return_func)
print(return_func(100))