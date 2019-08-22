# Function Annotation Demo tuple return 

Python code
```python
def f(ham:str , eggs:str = 'eggs') ->(str,str):
    print('Annotations:',f.__annotations__)
    print('Arguments:',ham,eggs)
    return ham+' and '+eggs,'others output'
```
Output if multi output
```text
Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': (<class 'str'>, <class 'str'>)}
Arguments: spam eggs
('spam and eggs', 'others output')
```
