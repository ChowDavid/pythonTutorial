Code
```Python
def sum(m,n):
    return m+n


if __name__ =='__main__':
    import sys
    print(sum(int(sys.argv[1]),int(sys.argv[2])))
```

execute
```$xslt
>python3 plus.py 1 2
3
```