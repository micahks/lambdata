# lambdata

A test package to learn about OOP, Containters, and Testing.

## Install 

To install this package just run: `pip install -i https://test.pypi.org/simple/ lambdata-micahks==0.0.2`

Then `import lambdata.example_module`

## Use

This package has a `MyDataFrame` class with a `state_abb` method. The `MyDataFrame` class can take a list/array/dictionary and turn it into a Dataframe object much like pd.DatatFrame with Pandas. The `state_abb` method can be used on the DF object and takes a column of states and returns the same DF with an added row of abbreviations.

```df = MyDataFrame({'State': ['Hawaii', 'California', 'Texas', 'new york']})
print(df)```
