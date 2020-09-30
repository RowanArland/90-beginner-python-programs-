firstlist = ['p', 'q']
print("Initial",firstlist)
n = 4
final = ['{}{}'.format(x, y) for y in range(1, n+1) for x in firstlist]
print(final)
