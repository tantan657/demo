# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}', end='\t')
#     print()

m = 1
while m <= 9:
    n = 1
    while n <= m:
        print(f'{m}*{n}={m*n}', end='\t')
        n += 1
    m += 1
    print()