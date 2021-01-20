def like_range(n):
    if n <= 1:
        return n
    else:
        return (like_range(n-1) + like_range(n-2))

for i in range(1, 10):
    print(like_range(i))
