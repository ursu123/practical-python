def cel_to_fah(n):
    a = [0] * n
    b = [0] * n
    
    for i in range(n):
        a[i] = i * 10 # degrees celsius
        b[i] = a[i] * 1.8 + 32
    return a, b

print(cel_to_fah(20))
