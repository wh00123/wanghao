import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
