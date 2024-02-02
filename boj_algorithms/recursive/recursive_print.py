def func1(x):
    if x == 0:
        return
    
    print(x)
    return func1(x-1)
    
func1(10)