exp76list = [{'key': {'subkey': 5}}, {'key': {'subkey': 105}}, {'key': {'subkey': 102}}]
print("Original List: ")
print(exp76list)
exp76list.sort(key=lambda e: e['key']['subkey'])
print("Sorted List: ")
print(exp76list)
