exp81list = [{'key1':'james', 'key2':'harry'}, {'key1':'joel', 'key2':'arter'}]
print("Original List: ")
print(exp81list)
newexp81list = [{k: v for k, v in d.items() if k != 'key1'} for d in exp81list]
print("New List: ")
print(newexp81list)
