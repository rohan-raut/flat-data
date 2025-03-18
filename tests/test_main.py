import pandas as pd
import json
from flat_data import FlatData

with open('./test/test1.json', 'r') as file:
    test_data_1 = json.load(file)

with open('./test/test2.json', 'r') as file:
    test_data_2 = json.load(file)

with open('./test/test3.json', 'r') as file:
    test_data_3 = json.load(file)

obj1 = FlatData(test_data_1, ['team', 'type', 'members', 'salary'])
obj2 = FlatData(test_data_2, ['students', 'math', 'english'])
obj3 = FlatData(test_data_3, ['employees', 'age', 'department'])



df1 = pd.DataFrame(obj1.get_flat_data())
df1.to_csv('./test/test1.csv')

df2 = pd.DataFrame(obj2.get_flat_data())
df2.to_csv('./test/test2.csv')

df3 = pd.DataFrame(obj3.get_flat_data())
df3.to_csv('./test/test3.csv')