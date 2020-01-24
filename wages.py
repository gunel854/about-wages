def wages(a):
    b = 0
    c = 0
    d = 0
    if a <= 1000:
        b = a * 0.14
        c = a * 0.02
        d = a - b - c 
        print(d)
        # ve ya print(int(d))
    
    elif a >= 2500:
        b = a * 0.20
        c = a * 0.05
        d = a - b - c 
        print(d)
        # və ya print(int(d))
    
    else:
        print("wrong")
        
wages(1000)
