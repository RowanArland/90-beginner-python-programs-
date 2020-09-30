dic = {1:'Hello' , 2: { 3: { 4: {}}}}
def depth(dic, level = 1): 
    str_dic = str(dic) 
    count = 0
    for i in str_dic: 
        if i == "{": 
            count += 1
    print("The Depth of Given Dictionary:",count) 
depth(dic)
