exp77list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def listslicing(S, slicing):
    return [S[i::slicing] for i in range(slicing)]
print(listslicing(exp77list,3))
