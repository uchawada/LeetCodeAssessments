n = 10 

triangle_data = [['*' for _ in range(i)] for i in range(1, n+1, 2)]

for d in triangle_data:
    pad_len = (n - len(d)) // 2
    string = ''.join(d)
    print(' '*pad_len + string + ' '*pad_len)
