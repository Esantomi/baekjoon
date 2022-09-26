N = int(input())
sq_nums = [2**i for i in range(31)]

print(1 if N in sq_nums else 0)