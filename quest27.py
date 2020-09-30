def change():
    
    odd = [2, 4, 6, 8]
    print('original',odd)
    odd[0] = 1            
    print('Changing first position',odd)

    odd[1:4] = [3, 5, 7]  
    print('changing second to last position',odd)

change()
