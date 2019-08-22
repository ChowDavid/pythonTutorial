Here we have a math.py tree look like

![Tree](packageTree.PNG?raw=true "Tree")

It has only one method
```python
def sum(a,b):
    return a+b
```

Method 1: direct import and call
```python
import au.com.david.math
print(au.com.david.math.sum(1,3))
```
Method 2: import class as name
```python
import au.com.david.math as math
print(math.sum(1,5))
```
Method 3: from import as name
```python
from au.com.david import math
print(math.sum(1,7))
```
Method 4: import method name as internal method
```python
from au.com.david.math import sum
print(sum(1,100))
```
Method 5: import method name as internal method with other name
```python
from au.com.david.math import sum as sum1
print(sum1(1,100))
```
