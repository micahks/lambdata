# lambdata

A test package to learn about OOP, Containters, and Testing.

## Install 

To install this package just run: `pip install -i https://test.pypi.org/simple/ lambdata-micahks==0.0.2`

Then `import lambdata.example_module`

## Use

This package has a `MyDataFrame` class with a `state_abb` method. The `MyDataFrame` class can take a list/array/dictionary and turn it into a Dataframe object much like pd.DatatFrame with Pandas. The `state_abb` method can be used on the DF object and takes a column of states and returns the same DF with an added row of abbreviations. 

See Example.
input:
```
df = MyDataFrame({'State': ['Hawaii', 'California', 'Texas', 'new york']})
print(df)
```
output:
```
        State
0      Hawaii
1  California
2       Texas
3    new york
```
input:
```
print(df.state_abb('State'))
```
output:
```
        State state_abbreviation
0      Hawaii                 HI
1  California                 CA
2       Texas                 TX
3    new york                 NY
```
