def f(ham:str , eggs:str = 'eggs') ->(str,str):
    print('Annotations:',f.__annotations__)
    print('Arguments:',ham,eggs)
    return ham+' and '+eggs,'others output'


print(f('spam'))