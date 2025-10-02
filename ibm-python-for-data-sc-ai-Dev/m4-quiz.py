
import numpy as np
a=np.array([-1,1])
b=np.array([1,1])
print(a)
print(b)
print(np.dot(a,b))
X=np.array([[1,0,1],[2,2,2]]) 
print(X.ndim)

# create dataframe from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
import pandas as pd
df = pd.DataFrame(data)
print(df)   