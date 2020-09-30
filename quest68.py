exp68list1 = ['a','b','c','d','e','f']
exp68list2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(exp68list1).difference(exp68list2)))
print('Additional values in second list: ', ','.join(set(exp68list2).difference(exp68list1)))
